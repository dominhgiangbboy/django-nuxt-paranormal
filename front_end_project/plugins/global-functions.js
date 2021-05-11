
import Vue from "vue";
const base_url = "http://127.0.0.1:8000/api/";
Vue.mixin({
  methods: {
    configButton(buttonType,enable,hide){
      switch (buttonType){
        case 'update':
          this.$store.commit('UPDATE_BUTTON', enable)
          this.$store.commit('UPDATE_BUTTON_HIDE', hide)
          break;
        case 'insert':
          this.$store.commit('INSERT_BUTTON', enable)
          this.$store.commit('INSERT_BUTTON_HIDE', hide)
          break;
        case 'delete':
          this.$store.commit('DELETE_BUTTON', enable)
          this.$store.commit('DELETE_BUTTON_HIDE', hide)
          break;
        case 'cancel':
          this.$store.commit('CANCEL_BUTTON', enable)
          this.$store.commit('CANCEL_BUTTON_HIDE', hide)
          break;
        default:
          break;
      }
     
    },
    // Sweet alert common function
    sweetsAlert(message, subMessage, alertType) {
      var me = this;
      me.$swal({
        title: message,
        text: subMessage,
        icon: alertType,
        showCancelButton: true,
        cancelButtonText: 'cancel'
      }).then(function(){
        if (alertType == "error"){
          me.logoutAction();
        }
      });;
    },
    swAlert(message, subMessage, alertType, callFunction) {
      var me = this;
      me.$swal({
        title: message,
        text: subMessage,
        icon: alertType,
        showCancelButton: true,
        cancelButtonText: 'cancel'
      }).then(function(result){
        if(result.isConfirmed){
          callFunction()
        }
      });
    },
    // Refresh new token
    async refreshToken() {
      let me = this;
     
      if (this.$auth.strategy.refreshToken.status().expired()){
        me.sweetsAlert("Session expired", "Please loggin again", "error");
      }
      else{
        var refreshToken = this.$auth.strategy.refreshToken.get();
        var data = {
          refresh: refreshToken
        };
        
        me.$axios
          .post(base_url + 'token/refresh/', data)
          .then(async res => {
            await me.$auth.strategy.token.set("Bearer " + res.data.access);
          })
          .catch(error => {
            if (this.$axios.isCancel(error)) {
            } else {
              me.sweetsAlert("Api called fail", "Please contact admin", "error");
            }
          });
      }
      
    },
    //logout function
    logout(){
      var me = this
      me.swAlert(
        "LOGOUT", 
        "Are you sure you want to log out?", 
        "question",
        me.logoutAction)
    },
    async logoutAction(){
      var me = this;
      await me.$auth.logout()
      me.$nuxt.$router.push('/login');
      me.$auth.strategy.refreshToken.reset();
      me.$auth.strategy.token.reset();
    },
    //  common methods POST data
    async postToServer(data,api) {
      let me = this;
      var config = {
        method: 'post',
        url: base_url + api,
        data: data,
      }
      var promise = new Promise(function(resolve, reject) {
          me.$axios(config)
          .then(res => {
           
            resolve(res.data);
          })
          .catch(error => {
            if(!error.response){
              me.sweetsAlert("Can't connect to server", "Please contact admin", "error");
            }
            else{
              if( error.response.status == 401){
                me.refreshToken();
                me.$axios(config)
                .then(res => {
                  resolve(res.data);
                })
                .catch(error => {
                  me.sweetsAlert("Authentication failed", "Please login again", "error")
                });
            }
            else{
              if (this.$axios.isCancel(error)) {  
                
              } else {
                me.sweetsAlert("Api called fail", "Please contact admin", "error");
              }
            }
            }
          }
        );          
      });
    
      return promise;
    },
    // Login function to get token
    async signup(user_name, password, is_dev,email, company) {
      var me = this;
      await me.$axios.post(base_url + 'user/create-user/',{
          user_name: user_name,
          password : password,
          is_dev: is_dev,
          email: email,
          company: company,
        })
        .then(async resp => {
          me.swAlert(
            "Success",
            "Successfully created user", 
            "success", ()=>{
            me.$nuxt.$router.push('/login')
          })
          
        })
        .catch(error => {
          me.sweetsAlert(
            "Sign up failed",
            error,
            "error"
          );
        });
    },
    async downloadFile(data, fileName){
      var me = this;
      var url = 'index/download-file/';
      me.$axios({
        url: base_url + url,
        method: 'POST',
        responseType: 'blob', // important
        data: data,
      }).then((response) => {
         debugger
         const url = window.URL.createObjectURL(new Blob([response.data]));
         const link = document.createElement('a');
         link.href = url;
         link.setAttribute('download', fileName + ".zip"); //or any other extension
         document.body.appendChild(link);
         link.click();
      });
    },
    async uploadFile(url,data){
      var me = this;
      me.$axios({
        url: base_url + url,
        method: 'POST',
        responseType: 'blob', // important
        data: data,
      }).then((response) => {
         const url = window.URL.createObjectURL(new Blob([response.data]));
         const link = document.createElement('a');
         link.href = url;
         link.setAttribute('download', '.zip'); //or any other extension
         document.body.appendChild(link);
         link.click();
      });
    },
    // Login function to get token
    async login(user_name, password) {
      var me = this;
       await me.$axios.post(base_url + 'user/login/',{
        user_name:user_name,
        password :password,
        })
        .then(async resp => {
          await me.$auth.strategy.token.set( "Bearer " + resp.data.access);
          await me.$auth.strategy.refreshToken.set(resp.data.refresh);
          me.$nuxt.$router.push('/')
        })
        .catch(error => {
          if (this.$axios.isCancel(error)) {
            
          } else {
            me.sweetsAlert(
              "Login failed",
              error,
              "error"
            );
          }
        });
    }
  }
});
