<template>
  <div class="home-page">
      <nav class="navbar navbar-expand-lg fixed-top navbar-light bg-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <nuxt-link class="nav-link" to="/">Home</nuxt-link>

        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
            <li class="nav-item">
              <nuxt-link class="nav-link" to="/DataSet">User's datasets</nuxt-link>
            </li>
            <li class="nav-item">
              <nuxt-link class="nav-link" to="/DataSet">Published datasets</nuxt-link>
            </li>
            <li class="nav-item">
              <nuxt-link class="nav-link" to="/DataSet">My datasets</nuxt-link>
            </li>
            <li class="nav-item">
              <nuxt-link class="nav-link" to="/AccountSetting">My Account</nuxt-link>
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
  
}
</script>
