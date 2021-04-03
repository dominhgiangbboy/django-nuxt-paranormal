<template>
  <v-container class="container" fluid>
    <v-dialog
      v-model="dialog"
    >
      <v-card class="pa-2">
        <v-card-title class="mb-5 dialog-header-text" >
          今日の部材点数入力
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="mt-5">
            <v-row>
                <v-col  :cols="mini?'6':'3'">
                    <custom-combo-box
                        
                    >
                    </custom-combo-box>
                </v-col>
                <v-col  :cols="mini?'6':'3'">
                    <custom-combo-box
                        label="工程"
                    >
                    </custom-combo-box>
                </v-col>
                <v-col  :cols="mini?'6':'3'">
                    <custom-date-field label="日付">

                    </custom-date-field>
                </v-col>
                <v-col cols="12">
            <v-row>
                <v-col :cols="mini?6:4">
                    <custom-info-field label-header="案件">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?6:4">
                    <custom-info-field label-header="工程">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?6:4"> 
                    <custom-info-field label-header="材料費">

                    </custom-info-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col :cols="mini?6:4">
                    <custom-info-field label-header="材料費" color-header="#5aa739">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?6:4">
                    <custom-info-field label-header="作業実績" color-header="#5aa739">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?6:4">
                    <custom-info-field :label-header="'日付'" color-header="#5aa739">

                    </custom-info-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col :cols="mini?6:4">
                    <custom-info-field label-header="差異" color-header="#5aa739" :read-only="true" :disabled="true" bg-color="#e5e5e5">

                    </custom-info-field>
                </v-col>
            </v-row>
            </v-col>
        </v-row>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions class="mt-2 mb-2">
          <v-btn
            style="margin-left:auto"
            class="mr-5"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <custom-button label="Add" v-on:click="dialog= false">
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
   
    <v-row>
        <v-col  :cols="mini?'6':'3'">
            <custom-combo-box
                label="案件"
                :comboBoxItems="projectList"
            >
            </custom-combo-box>
        </v-col>
        <v-col  :cols="mini?'6':'3'">
            <custom-combo-box
                label="工程"
                :comboBoxItems="plantList"
            >
            </custom-combo-box>
        </v-col>
        <v-col  :cols="mini?'6':'3'">
            <custom-date-field label="開始時間">

            </custom-date-field>
        </v-col>
        <v-col  :cols="mini?'6':'3'">
            <custom-date-field label="終了時間">

            </custom-date-field>
        </v-col>
        <v-col cols="12">
            <custom-button
                v-on:click="clickButton"
                label="Add Item"
            >
            </custom-button>
        </v-col>
    </v-row>
    <v-row>
        <v-col>
            <!-- Main Table -->
            <custom-table
            :is-show-all="true"
            :defaultPageSize="10"
            :headerItems="tableHeaders"
            :isLoading="isLoading"
            :dataTableItems="tableItems"
            >
            </custom-table>
        </v-col>
    </v-row>
  

  </v-container>
</template>
<style lang="scss" scoped>
  .text-red{
    font-weight: bold;
    color: $delete-button-color;
  }
  .tab-bar{
    background-color: $accent-color !important;
  }
  .tab-item{ 
    padding: 1rem;
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
      tab: null,
      isLoading: true,
      plantList:[],
      projectList: [],
      tableHeaders: [
        {
          text: '案件',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        {
          text: '工程',
          align: 'center',
          sortable: false,
          value: '実行予算金額',
        },
        {
          text: '材料費',
          align: 'center',
          sortable: false,
          value: '比率',
        },
        {
          text: '日付',
          align: 'center',
          sortable: false,
          value: '付加価値額',
        },
        {
          text: '目標実績',
          align: 'center',
          sortable: false,
          value: '付加価値額',
        },
        {
          text: '材料費',
          align: 'center',
          sortable: false,
          value: '部材点数',
        },
        {
          text: '作業実績',
          align: 'center',
          sortable: false,
          value: '部材点数',
        },
        {
          text: '差異',
          align: 'center',
          sortable: false,
          value: '部材点数',
        },
        {
          text: '',
          align: 'end',
          sortable: false,
          value: 'input',
        },
      ],
      tableItems:[
        {
          name: 'Giang',
          実行予算金額: 'Test',
          比率: 'Test',
          付加価値額: 'Test',
          付加価値額: 'Test',
          部材点数: 'Test',
          一台当たりの付加価値額: 'Test',
        }
      ],
      dialog: false,
      search: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      select: ["案件"],
      items: ["案件A", "案件B", "案件C"],
      //API links
      getPlantListAPI: "index/get-plant-list/",
      get_projects_api :"get-projects-list/",
    };
  },
  mounted(){
    if(this.tableItems.length > 0){
      this.isLoading = false
    }
    this.init()
  },
  methods: {
    init(){
      this.getPlantList()
      this.getProjecttList()
    },
    // get list project
    async getProjecttList(){
      var me = this;
      var dataReq;
      me.postToServer(dataReq,me.get_projects_api).then((res)=>{
        me.projectList = res
      })
    },
    //get production plant lists
    async getPlantList(){
      var me = this;
      var dataReq;
      me.postToServer(dataReq,me.getPlantListAPI).then((res)=>{

        me.plantList = res
      })
    },
    clickButton(){
        this.dialog = true;
    },
    submit() {
      if (this.$refs.form.validate()) {
        this.$refs.form.$el.submit();
      }
    },
    clear() {
      this.$refs.form.reset();
    },
  },
};
</script>
