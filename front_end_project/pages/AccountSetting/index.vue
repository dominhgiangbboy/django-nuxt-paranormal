<template>
  <v-container class="container" fluid>
    <!-- add Plant dialog -->
    <v-row>
      <div class="tile">
        <div class="avatar">
          <v-icon class="icon" color="orange darken-2" x-large>
            mdi-account
          </v-icon>
        </div>
      </div>
    </v-row>
    <v-row justify="start">
      <v-col :cols="mini?'12':'10'" align="center">
        <v-form v-model="valid" ref="form">
          <v-row>
            <v-col cols="2">
              <div class="text-header">
                <span>
                   {{$t('User name:')}}
                </span>
              </div>
            </v-col>
            <v-col>
              <v-text-field
                :disabled="true"
                class="text-input"
                :label="$t('Username')"
                v-model="temp.user_name"
                filled
                rounded
                required
              ></v-text-field>
              
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <div class="text-header">
                <span>
                  Email: 
                </span>
              </div>
            </v-col>
            <v-col>
              <v-text-field
                class="text-input"
                label="Email"
                rounded
                v-model="temp.email"
                filled
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <div class="text-header">
                <span>
                   {{$t('Company:')}}
                </span>
              </div>
            </v-col>
            <v-col>
              <v-text-field
                class="text-input"
                label="Company name"
                v-model="temp.company"
                rounded
                filled
              ></v-text-field>
            </v-col>
          </v-row>
          <custom-button
            v-on:click="submit"
            :label="$t('Save Data')"
          >
          </custom-button>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<style lang="scss" scoped>
  .avatar{
    border-radius: 50%;
    display: flex;
    background-color: #fff;
    width: 10rem;
    justify-content: center;
    height: 10rem;
  }
  .text-data{
    padding: 2rem;
  }
  .icon{
    color: #000;
    cursor: pointer;
  }
  .text-header{
    margin-top: 1rem;
    text-align: start;
  }
  .tile{
    width: 100%;
    padding: 1rem;
    background-color: #dee2e6;
    margin-bottom: 1rem;
  }
  .dialog-header-text{
    color: $border-color !important;
    font-weight: bold !important;
  }
  .rm-padding-right{
    padding-right: 0 !important;
  }
  .rm-padding-left{
    padding-left: 0 !important;
  }
  .header-title{
    background-color: $main-theme;
    color: $text-color;
    padding: 0.5rem;
    max-height: 2.5rem;
    text-align: center;
    border: 1px solid $text-color;
  }
  .header-text{
    padding: 10px;
    text-align: right;
    font-weight: bold;
  }
  .row-title{
    max-height: 2.5rem;
  }
  .info-section{
    min-height: 2.5rem;
    background-color: lightgrey;
    border: 1px solid $text-color;
    padding-left: 0.5rem;
    padding-top: 0.5rem;
  }
  .section-2{
    padding: 1rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    min-height: 300px;
  }
</style>
<script>
export default {
  components: {},
  computed: {
    mini() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
        case "sm":
          return true;
        case "md":
          return true;
        case "lg":
          return false;
        case "xl":
          return false;
      }
    },
    phone() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
        case "sm":
          return true;
        case "md":
          return false;
        case "lg":
          return false;
        case "xl":
          return false;
      }
    },
  },
  data() {
    return {
      temp: {},
      userNameEdit: false,
      isLoading: false,
      valid: false,
      isLoadingDifferent:false,
      dataTempProject: {},
      company: '',
      email: '',
      get_user_data: 'get-user-data/',
      update_user_data: 'update-user-data/',
      userName: '',
    };
  },
  created(){
    this.userID = this.getCookie("userID")
  },
  mounted(){
    this.init()
  },
  methods: {
    init(){
      var me = this
      me.refreshToken();
      me.getUserData();
    },

    // Process actions
    async getUserData(){
      var me = this;
      var dataReq = {
        "userID" : parseInt(this.userID)};
      me.postToServer(dataReq,me.get_user_data).then((res)=>{  
        me.temp = res[0]
      })
    },

    // Get combo box items
    async submit(){
      var me = this;
      var dataReq = me.temp;
        me.postToServer(dataReq,me.update_user_data).then((res)=>{  
        me.swAlert(
                  'Success'
                  , 'User info updated'
                  , 'success', ()=>{me.getUserData()})
        me.getUserData()
      })
    }
  },
};
</script>
