<template>
    <v-toolbar
      class="toolbar"
      dark
      prominent
      height="100px"
      width="100%"
      :elevation="0"
    >
      <v-app-bar-nav-icon class="mt-5" v-if="mobile" v-on:click="hideNavDrawer"></v-app-bar-nav-icon>
      <div class="mt-6 ml-5"> 
          <v-toolbar-title class="title-banner">        
              {{title}}
          </v-toolbar-title>    
      </div>
      <v-spacer>
      </v-spacer>
      <v-btn
        light
        class="mt-5 ml-5 button-style"
        :disabled="state.disableUpdate"
        v-if="!state.hideUpdateButton"
        v-on:click="$nuxt.$emit('updateClick')"
      >
        Update
      </v-btn>
      <v-btn
      light
      class="mt-5 ml-5 button-style"
      :disabled="state.disableInsert"
      v-if="!state.hideInsertButton"
      v-on:click="$nuxt.$emit('insertClick')"
      >
        Insert
      </v-btn>
      <v-btn
      light
      class="mt-5 ml-5 button-style"
      :disabled="state.disableDelete"
      v-if="!state.hideDeleteButton"
      v-on:click="$nuxt.$emit('deleteClick')"
      >
        Delete
      </v-btn>
      <v-btn
      light
      class="mt-5 ml-5 button-style"
      :disabled="state.disableCancel"
      v-if="!state.hideCancelButton"
      v-on:click="$nuxt.$emit('deleteClick')"
      >
        Cancel
      </v-btn>
    </v-toolbar>
</template>
<style lang="scss" scoped>
    .toolbar{
      background-color: $accent-color !important;
    }
    .title-banner{
      font-weight: 500;
      letter-spacing: 0.1rem;
    }
    .setting-list{
      margin-top: auto;
    }
    .title-icon{
      text-align: left;
      padding: 1rem;
      font-size: 2rem;
      font-weight: 600;
    }
    .button-style{
      background-color: $button-color !important;
    }
</style>
<script>
export default {
    props:{
      title:{
        type: String,
        default: ''
      },
      disableUpdate:{
        type:Boolean,
        default: false
      }
    },
    computed:{
      state() {
          return this.$store.state;
      },
      mobile () {
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return true
          case 'sm': return true
          case 'md': return true
          case 'lg': return false
          case 'xl': return false
          default: return false
        }
      },
      
    },
    data: () => ({
      
    }),
    methods: {
      hideNavDrawer: function ()
      {
        var me = this;
        me.$emit('hide-drawer');
      }
    },
  }
</script>
