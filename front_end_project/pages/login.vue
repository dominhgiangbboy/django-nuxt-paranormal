<template>
  <v-app>
    <v-container fluid fill-height class="loginOverlay">
      <v-layout :class="mobile?'welcome-section-mb':'welcome-section'">
        <v-row>
          <v-col cols="12">
            <v-row>
              <v-col align="center">
                <img src="~/assets/img/logo-main2.png" class="img">  
              </v-col>
            </v-row>
            <v-row>
              <v-col class="ml-5">
                <div class="welcome-text"><span>{{$t("Welcome to HUST's abnormal dataset system")}}</span></div>  
                <span class="introduction">

                </span>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-layout>
      <v-layout flex  :column="mobile" align-center="mobile" justify-center="mobile"  :class="mobile?'login-section-mb':'login-section'">
        <div v-if="mobile" class="welcome-text-mb">{{$t("Welcome to HUST's abnormal dataset system")}}</div>
        <v-flex xs12 sm8 elevation-6 style="box-shadow:none !important" class="pt-10">
          <v-card class="login-form">
            <div class="login-header">{{$t("LOGIN")}}</div>
            <v-card-text class="pt-4">
              <div>
                <v-form v-model="valid" ref="form">
                  <v-text-field
                    class="text-input"
                    :label="$t('Enter your username')"
                    v-model="userName"
                    :rules="userRules"
                    filled
                    required
                    background-color="#E8E8E8"
                  ></v-text-field>
                  <v-text-field
                    class="text-input"
                    :label="$t('Enter your password')"
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
                    <v-btn @click="submit" class="login-button">{{$t("LOGIN")}}</v-btn>
                  </v-layout>
                  <div class="mt-5" style="text-align: center">
                    <NuxtLink locale="vi" :to="localePath('/signup')">{{$t("New to HUST's abnormal system? Sign up")}}</NuxtLink>
                  </div>
                  <v-row class="mt-5 ml-5">
                    <v-col  align="center">
                      <v-row>
                        <v-checkbox
                          v-model="en"
                          :disabled="en"
                          :value="en"
                          v-on:change="changeLocaleEn"
                        >
                        </v-checkbox>
                        <country-flag class="flag mt-3" country='gb'/>
                      </v-row> 
                    </v-col>
                    <v-col  align="center">
                     <v-row>
                        <v-checkbox
                           v-model="vi"
                          :disabled="vi"
                          :value="vi"
                          v-on:change="changeLocaleVi"
                        >
                        </v-checkbox>
                        <country-flag class="flag mt-3"  country='vn'/>
                      </v-row> 
                    </v-col>
                  </v-row>
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
      vi: false,
      en: true,
      currentLocale: '',
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
    changeLocaleVi(flag){
      if(flag){
        this.en = false
        if(this.vi){
          this.$i18n.setLocale('vi')
        }
      }
    },
    changeLocaleEn(flag){
      if(flag == true){
        this.vi = false
        if(this.en){
          this.$i18n.setLocale('en')
        }
      }
    },
    // changeLocale(id){
    //   this.$i18n.setLocale(id)
    //   this.currentLocale = id
    // },
    iconClick() {
      this.passwordVisibility = !this.passwordVisibility;
    },
    async submit() {
      var me = this;
      try {
          me.login(
            me.userName,
            me.password
          );
      } catch (e) {
        me.sweetsAlert('Errors', e , 'error');
      }
    },
    clear() {
      this.$refs.form.reset();
    }
  }
};
</script>
<style scoped lang="scss">
.flag{
  cursor: pointer;
}
.img{
  max-width: 100%;
  margin: 1rem;
}
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
  font-size: 1rem;
  line-height: 1.2em;
  font-weight: bold;
  color: $main-theme;
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
  background:  #8ecae6;
  width: 100%;
  height: 50%;
  display: none;
}
.login-section {
  background: rgb(34, 145, 195);
  width: 50%;
  background: #003049;
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