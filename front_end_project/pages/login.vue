<template>
  <v-app>
    <v-container fluid fill-height class="loginOverlay">
      <v-layout flex align-center :class="mobile?'welcome-section-mb':'welcome-section'">
        <div class="welcome-text">Welcome to fukakachi system</div>
      </v-layout>
      <v-layout flex  :column="mobile" align-center="mobile" justify-center="mobile"  :class="mobile?'login-section-mb':'login-section'">
        <div v-if="mobile" class="welcome-text-mb">Welcome to fukakachi system</div>
        <v-flex xs12 sm8 elevation-6 style="box-shadow:none !important" class="pt-10">
          <v-card class="login-form">
            <div class="login-header">LOGIN</div>
            <v-card-text class="pt-4">
              <div>
                <v-form v-model="valid" ref="form">
                  <v-text-field
                    class="text-input"
                    label="Enter your username"
                    v-model="userName"
                    :rules="userRules"
                    filled
                    required
                    background-color="#E8E8E8"
                  ></v-text-field>
                  <v-text-field
                    class="text-input"
                    label="Enter your password"
                    background-color="#E8E8E8"
                    v-model="password"
                    min="8"
                    filled
                    :append-icon="
                      passwordVisibility ? 'mdi-eye' : 'mdi-eye-off'
                    "
                    @click:append="iconClick"
                    :type="passwordVisibility ? 'password' : 'text'"
                    :rules="passwordRules"
                    required
                  ></v-text-field>
                  <v-layout class="pt-10">
                    <v-btn @click="submit" class="login-button">Login</v-btn>
                  </v-layout>
                </v-form>
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>
<script>
export default {
  layout: "loginLayout",
  
  components: {},
  computed: {
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
  data() {
    return {
      valid: true,
      passwordVisibility: true,
      password: "",
      passwordRules: [v => !!v || "Password is required"],
      userName: "",
      userRules: [
        v => !!v || "Username is required",
      ]
    };
  },
  methods: {
    iconClick() {
      this.passwordVisibility = !this.passwordVisibility;
    },
    async submit() {
      var me = this;
      try {
          me.login(me.userName,me.password);
      } catch (e) {
        me.sweetsAlert('Errors', 'error', 'error');
      }
     
      // await me.$auth.setToken('local', "Bearer " + res.data.access);
      // await me.$auth.setRefreshToken('local', res.data.refresh);
      // await me.$auth.setUserToken(res.data.access);
    },
    clear() {
      this.$refs.form.reset();
    }
  }
};
</script>
<style scoped lang="scss">
.login-header {
  text-align: center;
  padding-top: 1rem;
  padding-bottom: 1rem;
  font-size: 1.5rem;
  font-weight: 800;
  color: $main-theme;
}
.text-input {
  border-radius: 20px;
}
.loginOverlay {
  margin: 0;
  padding: 0;
}
.welcome-text {
  padding-left: 2rem;
  font-size: 6rem;
  line-height: 1.2em;
  font-weight: bold;
  background: linear-gradient(279deg, $main-theme 0%, $main-theme 78%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.welcome-text-mb {
  font-size: 2rem;
  line-height: 1.2em;
  padding-top: 1rem;
  font-weight: bold;
  text-align: center;
  color: whitesmoke;
}
.login-button {
  width: 100%;
  height: 4em !important;
  background-color: $main-theme !important;
  color: whitesmoke;
}
.login-form {
  border-radius: 20px;
  padding: 2rem;
}
.welcome-section {
  background-color: white;
  width: 50%;
}
.welcome-section-mb {
  background:  rgba(51, 45, 253, 1) 78%;
  width: 100%;
  height: 50%;
  display: none;
}
.login-section {
  background: rgb(34, 145, 195);
  width: 50%;
  background: linear-gradient(
    0deg,
    rgba(34, 145, 195, 1) 0%,
    rgba(51, 45, 253, 1) 78%
  );
}
.login-section-mb {
  background: rgb(34, 145, 195);
  background: linear-gradient(
    0deg,
    rgba(34, 145, 195, 1) 0%,
    rgba(51, 45, 253, 1) 78%
  );
}
</style>