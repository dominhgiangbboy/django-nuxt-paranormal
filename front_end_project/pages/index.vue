<template>
  <v-container fluid>
    <v-row>
        <v-col cols="6">
          <div class="text-padding">
            <span > 
              With our system you can get Data Set from many sources like crawled data or default processed data.
            </span>
          </div>
          <v-col cols="12" align="center">
            <custom-button
              v-on:click="addItem"
              label="Get data set"
            >
            </custom-button>
          </v-col>
        </v-col>
        <v-col align="center" cols="6">
          <div class="img-section">
            <img src="../assets/img/computerData.jpeg" class="img" alt="">
          </div>
        </v-col>
        <v-col align="center" cols="6">
          <div class="img-section">
            <img src="../assets/img/sciencetist.jpeg" class="img" alt="">
          </div>
        </v-col>
        <v-col cols="6">
          <div class="text-padding">
            <span> 
            If you are a developer or a sciencetist you can see your analyzed data here.
            </span>
          </div>
          <v-col cols="12" align="center">
            <custom-button
              v-on:click="addItem"
              label="My analyzed data"

            >
            </custom-button>
          </v-col >
        </v-col>
        
        <v-col cols="6">
          <div class="text-padding">
            <span class="text-padding"> 
            You can also check out our collected pre-process data here.
            </span>
          </div>
          <v-col cols="12" align="center">
              <custom-button
                v-on:click="addItem"
                label="Pre-processed data"
              >
              </custom-button>
          </v-col >
        </v-col>
        <v-col align="center" cols="6">
          <div class="img-section">
            <img src="../assets/img/collect-data.jpeg" class="img" alt="">
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col align="center">
          <div class="title">
            Our data example
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col align="center">
          <iframe width="880" height="495" src="https://www.youtube.com/embed/NckU4v4dyxE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
          </iframe>
        </v-col>
        
      </v-row>
  </v-container>
</template>
<style lang="scss" scoped>
  .img {
    max-width: 80%;
  }
  .action-button{
    margin-left: 2rem;
  }
  .delete-button{
    color: $text-color;
    font-weight: bold;
    background-color: red  !important;
  }
  .diaglog-text{
    color: red;
    font-size: 1.2rem;
  }
  .combobox-header{
      text-align: right;
      font-weight: bold;
  }
  .combobox-header-left{
      text-align: left;
      font-weight: bold;
  }
  .text-padding{
    padding:20px
  }
  .title{
    font-weight: bold;
    font-size: 1.2rem;
    margin: 2rem;
  }
</style>
<script>

export default {
  layout: 'homePageLayout',
  data() {
    return {
      addDialog: false,
      isLoading: false,
      showUpdate:false,
      editDialog:false,
      comboBoxItems: [],
      infoField: '',
      deleteDialog: false,
      tempItemsEdit:{},
      
      tableHeaders:[],
    };
  },
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
  mounted() {
    this.init()
  },
  created () {
   
  },
  methods: {
    init(){
      var me = this;
      this.$nuxt.$on('insertClick', () => {
        //this.insertClick();
      })
    },
    async clickButton () {
      
    },
    deleteDialogOpen(item){
      this.deleteDialog = true;
      this.current_delete_id = item.item.id
    },
    async addItem(){
      var me = this;
      var dataReq = me.tempItems
      me.downloadFile('download-file/',{})
    },

    async editItemAction(){
      var me = this;
      var dataReq = me.tempItemsEdit
      me.postToServer(dataReq,me.update_projects_api).then((res)=>{
        me.editDialog = false;
        me.dataTableGet()
        me.tempItemsEdit = {
        }
      })
    },
    async updateItem(item){
      var me = this;
      var dataReq = item
      me.postToServer(dataReq,me.update_projects_api).then((res)=>{
        me.addDialog = false;
        me.dataTableGet()
      })
    },
    async deleteItem(){
      var me = this;
      var dataReq;
      if(me.current_delete_id != 0){
        dataReq = {
          "project_id": me.current_delete_id
        }
          me.postToServer(dataReq,me.delete_projects_api).then((res)=>{
          me.current_delete_id = 0;
          me.deleteDialog = false;
          me.dataTableGet()
        })
      }
      else{

      }
    },
    
    editItem(item){
      this.editDialog = true
      this.tempItemsEdit = item.item
    },
    // Get combo box items
    async dataTableGet(){
      var me = this;
      var dataReq;
      if(me.productID != 0){
          dataReq = {
          }
      }
      me.postToServer(dataReq,me.get_data_set).then((res)=>{
        me.tableItems = res
      })
    },
    openLink(item){
      var me = this;
      me.$nuxt.$router.push({ path: '/productsList', query: { projectID: item.id } })
    },
    clear() {
      this.$refs.form.reset();
    },
    // Created chart function
    
  }
};
</script>
