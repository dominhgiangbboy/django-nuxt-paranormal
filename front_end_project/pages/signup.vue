<template>
  <v-app>
    <v-container fluid fill-height class="loginOverlay">
      <v-layout flex :column="mobile" align-center="mobile" justify-center="mobile"  :class="mobile?'login-section-mb':'login-section'">
        <v-flex  xs12 sm8 elevation-6 style="box-shadow:none !important" class="pt-10">
          <v-card class="login-form">
            <div class="login-header">Sign up</div>
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
                  ></v-text-field>
                  <v-text-field
                    class="text-input"
                    label="Enter your password"
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
                  <v-text-field
                    class="text-input"
                    label="Re-Enter your password"
                    v-model="passwordReenter"
                    min="8"
                    filled
                    :append-icon="passwordVisibility ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="iconClick"
                    :type="passwordVisibility ? 'password' : 'text'"
                    :rules="passwordReenterRule"
                    required
                  ></v-text-field>
                  <v-text-field
                    class="text-input"
                    label="Enter your email"
                    v-model="email"
                    filled
                    :rules="passwordReenterRule"
                  ></v-text-field>
                  <v-text-field
                    class="text-input"
                    label="Enter your company name"
                    v-model="company"
                    filled
                    :rules="passwordReenterRule"
                  ></v-text-field>
                  <custom-combo-box
                    label="Select your role"
                    :comboBoxItems="roleCombo"
                    :itemValue="defaultComboValue"
                    v-on:change="selectCombobox"
                  >
                  </custom-combo-box>
                  <v-layout class="pt-10">
                    <v-btn @click="submit" class="login-button">Sign Up</v-btn>
                  </v-layout>
                  <div class="mt-5" style="text-align: center">
                    <NuxtLink to="/login">Have an acount? please login</NuxtLink>
                  </div>
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
      roleCombo: [
        {
          id: 1 , name: "Data sciencetist"
        },
        {
          id: 2 , name: "User"
        },
      ],
      company: '',
      email: '',
      currentRole: 0,
      passwordVisibility: true,
      password: "",
      passwordReenter: "",
      passwordReenterRule: [v => !!v || "Please enter your password again"],
      passwordRules: [v => !!v || "Password is required"],
      userName: "",
      userRules: [
        v => !!v || "Username is required",
      ]
    };
  },
  created(){
    this.defaultComboValue = this.roleCombo[0].id
    this.currentRole = this.defaultComboValue
  },
  methods: {
    iconClick() {
      this.passwordVisibility = !this.passwordVisibility;
    },
    async submit() {
      var me = this;
      if(me.passwordReenter != me.password){
        me.swAlert("Error", "Password not match please check your password again","error", ()=>{return}) 
      }
      else if (me.password.length < 8)
      {
        me.swAlert("Error", "Please input password with more than 8 character","error", ()=>{return}) 
      }
      else if (me.currentRole == 0 || me.currentRole == undefined){
        me.swAlert("Error", "Please select role","error", ()=>{return}) 
      }
      else{        
        me.signup(me.userName, me.password,me.currentRole == 1, this.email, this.company)
      }
    },
    selectCombobox(item){
      if(item == undefined){
        this.currentRole = 0
      }
      else{
        this.currentRole = item
      }
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
  min-width: 500px;
}
.welcome-section {
  background-color: white;
  width: 50%;
}
.welcome-section-mb {
  background: rgb(34, 145, 195);
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
  width: 100%;
  background: linear-gradient(
    0deg,
    rgba(34, 145, 195, 1) 0%,
    rgba(51, 45, 253, 1) 78%
  );
}
</style>