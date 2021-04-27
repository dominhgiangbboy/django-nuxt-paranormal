<template>
  <v-container class="container" fluid>
    <!-- add Plant dialog -->
    <v-row>
      <v-col cols="3"></v-col>
      <v-col align-self="center" :cols="mini?'12':'3'">
        <v-avatar size="128" class="align-center">
          <img
            src="https://cdn.vuetifyjs.com/images/john.jpg"
            alt="John"
          >
        </v-avatar>
      </v-col>
      <v-col :cols="mini?'12':'6'">
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
          <v-layout class="pt-10">
            <v-btn @click="submit" class="login-button">Save</v-btn>
          </v-layout>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<style lang="scss" scoped>
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
      isLoading: false,
      isLoadingDifferent:false,
      dataTempProject: {},
      tableHeaders: [
        {
          text: '制作物',
          align: 'start',
          sortable: false,
          value: 'product_name',
        },
        {
          text: '工程',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        {
          text: '実行予算金額',
          align: 'start',
          sortable: false,
          value: '実行予算金額',
          edditable: true,
        },
        {
          text: '比率',
          align: 'start',
          sortable: false,
          value: '比率',
        },
        {
          text: '付加価値額',
          align: 'start',
          sortable: false,
          value: '付加価値額',
        },
        {
          text: '部材点数',
          align: 'start',
          sortable: false,
          value: '部材点数',
          edditable: true,
        },
        {
          text: '一台当たりの付加価値額',
          align: 'start',
          sortable: false,
          value: '一台当たりの付加価値額',
        },
        {
          text: '1日あたりの目標生産数量',
          align: 'start',
          sortable: false,
          value: '日当りの目標生産数量',
          edditable: true,
        },
        {
          text: '1日あたらりの目標付加価値',
          align: 'start',
          sortable: false,
          value: '日当りの目標付加価値額',
        },
        {
          text: '',
          align: 'start',
          sortable: false,
          width: 100,
          value: 'inputDelete',
          disabledDelete: true
        },
      ],
      tableHeadersDifferent: [
        {
          text: '実行予算計画後',
          align: 'start',
          sortable: false,
          value: 'name',
          edditable: true,
        },
        {
          text: '金額',
          align: 'start',
          sortable: false,
          value: 'value',
          edditable: true,
        },
        {
          text: '',
          align: 'start',
          sortable: false,
          width: 100,
          value: 'input',
          disabledDelete: true
        },
      ],
      tableItems:[
      ],
      tableItemsDifferent: [

      ],
      // Temp item 
      tempHeaderItems: [],
      tempAddItems: {},
      deleteTableTempID: 0,
      status: false,
      
      currentProjectID: 0,
      addDialog: false,
      search: "",
      addTitle: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      select: ["案件"],
      items: ["案件A", "案件B", "案件C"],
      projectList: [],
      get_projects_api :"get-projects-list/",
      get_projects_data_api :"get-data-projects-list/",
      get_process_data_api :"get-process-data-detail/",
      update_process_data_api :"update-process-data-detail/",
      get_arise_data_api :"get-arise-cost-list/",
      calculate :"calculate-money/",
    };
  },
  mounted(){
    this.init()
  },
  methods: {
    init(){
      var me = this
      me.refreshToken();
      me.getProjectListValue();
      me.configButton('update',true, true)
      me.configButton('delete', true, true)
      
     
    },
    // Get combo box items
    async getProjectListValue(){
      var me = this;
      var dataReq;
      me.postToServer(dataReq,me.get_projects_api).then((res)=>{
        me.projectList = res
         if(me.projectList.length > 0){
          me.currentProjectID = me.projectList[0].id
          me.getProjectData()
          me.getProcessData()
          me.getAriseData()
        }
      })
      
    },
    // Get combo box items
    async getProcessData(){
      var me = this;
      me.isLoading = true
      var dataReq = {
        "project_id": me.currentProjectID
      };
      me.postToServer(dataReq,me.get_process_data_api).then((res)=>{
        me.tableItems = res
        me.isLoading = false
      })
      
    },
    // Get combo box items
    async getAriseData(){
      var me = this;
      me.isLoading = true
      var dataReq = {
        "project_id": me.currentProjectID
      };
      me.postToServer(dataReq,me.get_arise_data_api).then((res)=>{
        me.tableItemsDifferent = res
        me.isLoading = false
      })
      
    },
    
    async calculateAction(){
      var me = this;
      me.isLoading = true
      var dataReq = {
        "project_id": me.currentProjectID,
        "年間必要固定費額": parseInt(me.dataTempProject['年間必要固定費額'])
      };
      me.postToServer(dataReq, me.calculate).then((res)=>{
        me.getProjectData()
        me.isLoading = false
      })
    },
    deleteItemFromTable(){
        var me = this;
        if(me.deleteTableTempID != 0){
            var dataReq;
            dataReq = {
              "id":me.deleteTableTempID
            }
            me.postToServer(dataReq, me.deleteTableTempApi).then((res)=>{
                me.init()
            })
        }
    },
    deleteItem(){

    },
    addItem(){
      this.tempAddItems = {}
      this.addDialog=true
      this.tempHeaderItems = this.tableHeadersDifferent
    },
    editItem(editItem){
      this.tempAddItems = editItem.item
      this.tempHeaderItems = this.tableHeaders
      this.tempAPIUrl = this.update_process_data_api
      this.addDialog=true
    },
    deleteItemPlant(item){
      //open delete dialog
      this.deleteTableTempID = item.item.id
      this.swAlert("Delete","Delete plant?","warning", this.deleteItemFromTable)
    },
    async getProjectData(){
      var me = this;
      var dataReq = {
        "project_id": me.currentProjectID
      };
      me.postToServer(dataReq,me.get_projects_data_api).then((res)=>{
        var dataReturn = res[0]
        me.dataTempProject = dataReturn
      })
    },
    selectProject(id){
      var me = this
      me.currentProjectID = id
      me.getProjectData()
      me.getProcessData()
    },
    updateItemAction(){
        var me = this;
        var dataReq = me.tempAddItems;
        me.status = false
        me.tempHeaderItems.forEach(header => {
            if(header.edditable){
                if(me.tempAddItems[header.value] ==0 ||me.tempAddItems[header.value] =="" ||me.tempAddItems[header.value] == null ||me.tempAddItems[header.value] == undefined){
                    me.status = true
                    this.swAlert("Insert value","Please input value to " + header.text,"warning", me.submit)
                    return;
                }   
            }
        });
        dataReq.project_id = me.currentProjectID
        if(!me.status){
            me.postToServer(dataReq,me.tempAPIUrl).then((res)=>{  
              if(me.tempAPIUrl = me.update_process_data_api){
                me.getProcessData()
                me.isLoading = false
              }
            })
        }
        
    },
  },
};
</script>
