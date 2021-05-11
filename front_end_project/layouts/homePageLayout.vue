<template>
  <div class="home-page">
      <nav class="navbar navbar-expand-lg fixed-top navbar-light background">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <nuxt-link class="nav-link pr-10 mr-4 " to="/">Home</nuxt-link>

        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav mt-2 ml-4 mt-lg-0">
            <li class="nav-item ml-5" v-for="(item,index) in itemLink" :key="index">
              <nuxt-link class="nav-link" :to="item.link">{{item.name}}</nuxt-link>
            </li>            
          </ul>
        </div>

        <v-btn v-on:click="logout" rounded dark>
          <v-icon left>
            mdi-logout
          </v-icon>
          LOGOUT
        </v-btn>
      </nav>
      <div class="mt-10" style="margin-top: 200px">
         <nuxt/>
      </div>      
     
  </div>
</template>
<style lang="scss" scoped>
  .home-page{
    width: 100vw;
  }
  .background{
    background-color: #fff;
  }
</style>
<script>
export default {
  data() {
    return {
        itemLink: [
          {
            name: "Datasets", link: "/DataSet"
          },
          {
            name: "My analyzed data", link: "/Personal"
          },
          {
            name: "My Account", link: "/AccountSetting"
          },
        ]
      }

  },
}
</script>
