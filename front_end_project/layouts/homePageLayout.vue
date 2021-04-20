<template>
  <div class="home-page">
      <nav class="navbar navbar-expand-lg fixed-top navbar-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <nuxt-link class="nav-link pr-10 mr-4 " to="/">Home</nuxt-link>

        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav mr-auto mt-2 ml-4 mt-lg-0">
            <li class="nav-item ml-5" v-for="(item,index) in itemLink" :key="index">
              <nuxt-link class="nav-link" to="/DataSet">{{item.name}}</nuxt-link>
            </li>            
          </ul>
        </div>
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

</style>
<script>
export default {
  data() {
    return {
        itemLink: [
          {
            name: "User's datasets", link: "/DataSet"
          },
          {
            name: "Published datasets", link: "/DataSet"
          },
          {
            name: "My datasets", link: "/DataSet"
          },
          {
            name: "My Account", link: "/AccountSetting"
          },
        ]
      }

  },
}
</script>
