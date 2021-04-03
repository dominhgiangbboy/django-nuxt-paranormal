<template>
  <v-app>
    <v-row no-gutters>
      <div>
        <navdrawer 
          :drawer="hideDrawerFlag" 
          v-on:logout="logout" 
          v-on:hide-drawer="hideDrawer" 
          v-on:reset-drawer="resetDrawer"
        ></navdrawer>
      </div>
      <div :class="mini?hideDrawerFlag?'body-mb-full':'body-mb-full':'body flex-grow-1 flex-shrink-0'">
        <top-banner 
        :title="title" 
        v-on:hide-drawer="hideDrawer"
        >
        </top-banner>
        <!-- <div v-if="$auth.loggedIn">loggedIn</div> -->
        <v-row>
         <v-breadcrumbs 
            class="ma-5 breadcrumbs"
            :items="linkBreadcrumbs"
            nuxt
            divider="/"
          ></v-breadcrumbs>
        </v-row>
        <nuxt />
      </div>
    </v-row>
  </v-app>
</template>
<style lang="scss" scoped>
  .breadcrumbs{
    //text-decoration: underline;
  }
  .nav-drawer {
    height: 100%;
    width: 20%;
    transition: 200ms;
  }
  .nav-drawer-hide {
    height: 100%;
    width: 0%;
    transition: 200ms;
  }
  .body {
    height: 100%;
    width: 0%;
    transition: 200ms;
  }
  .body-mb {
    height: 100%;
    width: 80%;
    transition: 200ms;
  }
  .body-mb-full {
    height: 100%;
    width: 100%;
    transition: 200ms;
  }
 
</style>
<script>
import navdrawer from "~/components/LayoutComponents/NavigationDrawer.vue";
import TopBanner from "../components/LayoutComponents/TopBanner.vue";
export default {
  components: { navdrawer, TopBanner },
  computed:{
      navLayout() {
          return this.$store.state.layout;
      },
     
      mini() {
          switch (this.$vuetify.breakpoint.name) {
            case 'xs': return true
            case 'sm': return true
            case 'md': return true
            case 'lg': return false
            case 'xl': return false
        };
      },
      title(){
        const fullPathRaw = this.$route.fullPath
        const fullPath = fullPathRaw.split('?')[0]
        const params = fullPath.split('/')
        return params[params.length - 1].toUpperCase();
      },
      //add breadcrumbs link
      linkBreadcrumbs(){
        const fullPathRaw = this.$route.fullPath
        const fullPath = fullPathRaw.substring(1).split('?')[0]
        const params = fullPath.split('/')

        var tempBreadcumb=[{
              text: 'Home',
              disabled: false,
              to: '/',
        }]
        var linkPath = '';
        params.forEach(element => {
            var disabled = false;
            if (element == params[params.length - 1]){
              disabled = true
            }
            if(element != '' && element != '/' && element != null){
                linkPath = linkPath +'/'+ element  
                var tempBreadcumbEl =
                {
                  text: this.capitalizeFirstLetter(element),
                  disabled: disabled,
                  to: linkPath,
                };
                tempBreadcumb.push(tempBreadcumbEl);
            }
          }
        );
        return tempBreadcumb;
      }
    },
  data: () => ({
    items: [
      ['mdi-home', 'ホーム','/'],
      ['mdi-scale-balance', '付加価値額配分表','/AddedValue'],
      ['mdi-table', '鉄骨工事予算実行原価表','/masterLayouts'],
      ['mdi-cog', 'セッティング','/Settings'],
      ['mdi-trending-up', 'グラフ','/Graphs'],
      ['mdi-account-circle', 'Accounts','/Accounts'],
    ],
    hideDrawerFlag:true,
  }),
  methods: {
    capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    },
    hideDrawer: function(){
      this.hideDrawerFlag = !this.hideDrawerFlag;
      this.hideDrawerFlag = !this.hideDrawerFlag;
      this.hideDrawerFlag = !this.hideDrawerFlag;
    },
    resetDrawer: function(){
      this.hideDrawerFlag = true;
    }
  },
};
</script>
