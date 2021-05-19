<template>
  <v-container fluid>
    <v-dialog
      v-model="dialog"
      max-width="500px"
    >
      <v-card class="pa-2">
        <v-card-title class="mb-5 dialog-header-text" >
          Contribute my analysis data
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="mt-5">
          <v-row>
            <v-text-field
              outlined
              rounded
              dense
              label="Input your data's name"
              v-model="temp.name"
            >
              
            </v-text-field>
          </v-row>
          <v-row>
            <v-text-field
              outlined
              rounded
              dense
              label="Input your data's description"
              v-model="temp.description"
            >
              
            </v-text-field>
          </v-row>
          <v-row>
            <v-textarea
              outlined
              label="Insert your json data here"
              v-model="temp.json"
            >

            </v-textarea>
          </v-row>
          
          <v-row>
            <form enctype="multipart/form-data" novalidate>
              <v-container class="container" fluid>
              <form enctype="multipart/form-data" novalidate v-if="isInitial || isSaving">
                  <div class="dropbox">
                    <input type="file" multiple :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length"
                      accept="*" class="input-file">
                      <p v-if="isInitial">
                        Drag your file here
                      </p>
                      <p v-if="isSaving">
                        {{ fileCount }} selected
                      </p>
                  </div>
                </form>
              </v-container>
            </form>
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
          <custom-button label="Add" v-on:click="saveData">
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
        <v-col cols="12">
            <div class="title-banner">
                <v-row>
                    <div class="data-name">
                        <span>
                            {{detailItems.name}}
                        </span>
                    </div>
                </v-row>
                <v-row>
                    <div class="data-type">
                        <span>
                            {{detailItems.typeID == 1? 'Published Data': 'Crawled Data'}}
                        </span>
                    </div>
                </v-row>
            </div>
        </v-col>
    </v-row>
    <v-card outlined>
        <v-tabs v-model="tabModel">
            <v-tab>Data</v-tab>
            <v-tab>User analysis</v-tab>
            <v-tabs-items class="card"  v-model="tabModel">
                <v-tab-item>
                    <v-row>
                        <v-col cols="10" class="ml-5 mt-5 mb-5">
                            <v-card
                                elevation="2"
                                outlined
                            >
                                <v-card-title>Description</v-card-title>
                                <v-card-text>
                                    <v-row>
                                        <v-col>
                                            <div>
                                                {{detailItems.description}}
                                            </div>
                                        </v-col>
                                    </v-row>
                                </v-card-text>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-tab-item>
                <v-tab-item>
                    <v-row class="mt-5">
                        <v-col :cols="mini?'12':'6'">
                            
                            <custom-table
                                    :defaultPageSize="10"
                                    :headerItems="tableHeaders"
                                    :isLoading="isLoading"
                                    :dataTableItems="tableItems"
                                    :singleSelect="true"
                                    dense
                                    :showSelect="true"
                                    :isShowAll="false"
                                    :isBanner="true"
                                    v-on:selected="selectItem"
                                    toobarTitle="My dataset list"
                                    :disableAddButton="true"
                                    height="400"
                                >
                              </custom-table>
                              <custom-button
                                label="Add my dataset"
                                class="mt-5"
                                v-on:click="addDataSet"
                              >

                              </custom-button>
                            </v-col>
                            <v-col :cols="mini?'12':'6'">
                            <v-row>
                                <div class="text-header">
                                Preview data
                                </div>
                            </v-row>
                            <v-row>
                                <div class="json-field">
                                    <pre>{{ jsonstr | pretty }}</pre>
                                </div>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-tab-item>
            </v-tabs-items>
        </v-tabs>
    </v-card>
    
  </v-container>
</template>
<style lang="scss" scoped>
  .card{
    padding: 1rem;
  }
  .text-header{
    margin: 1rem;
    font-size: 1.5rem;
    font-weight: bold;
    color: $main-theme;
  }
  .data-name{
    margin: 1rem;
    font-size: 1.5rem;
    font-weight: bold;
    color: $main-theme;
  }
  .json-field{
    padding: 1rem;
    border: 1px gray solid;
    max-height: 50vh;
    margin-right: 2rem;
    width: 100%;
    overflow: auto;
    border-radius: 20px;
  }
  .data-type{
    margin: 1rem;  
  }
  .dropbox {
    outline: 2px dashed grey; /* the dash box */
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
    padding: 10px 10px;
    min-height: 200px; /* minimum height */
    position: relative;
    cursor: pointer;
  }
  .dropbox:hover {
    background: lightblue; /* when mouse over to the drop zone, change color */
  }

  .dropbox p {
    font-size: 1.2em;
    text-align: center;
    padding: 50px 0;
  }
  .title-banner{
    background-color: #dee2e6;
    width: 100%;
    max-height: 20vh;
    min-height: 10vh;
    padding: 1rem;
    overflow: auto;
  }
</style>
<script>
const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;
export default {
  data() {
    return {
      dialog: false,
      tabModel: 0,
      dataSetID: 0,
      userID: 0,
      showUpdate:false,
      isLoading:false,
      comboBoxItems: [],
      temp: {},
      get_data_set_api: "data-analysis-get/",
      get_data_add_api: "data-analysis-add/",
      datatype: "Crawled data",
      dataName: "Data's Name is",
      data: {
        "name": "Data's Name is",
        "type": "Crawled data",
        "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vitae lectus rhoncus, malesuada nulla eget, pellentesque odio. Integer iaculis porttitor varius. Suspendisse erat urna, sagittis et tempor id, posuere sit amet elit. Quisque tincidunt elit est, quis consequat neque molestie eu. Etiam sollicitudin nec nulla sed pretium. Cras sodales nec nulla in rhoncus. Aliquam at magna ac libero ultrices aliquam. Etiam porttitor, justo vitae rutrum accumsan, risus ligula viverra metus, nec aliquet dui justo at eros. In finibus ante eget sodales finibus. Suspendisse et lacus eleifend, faucibus ipsum et, hendrerit orci. Nullam sit amet ullamcorper nisl, vitae luctus elit.\nNam facilisis velit a magna dictum, fringilla luctus mi maximus. Nullam scelerisque vehicula eleifend. Suspendisse vestibulum vitae ante interdum rhoncus. Integer ultrices dui vel libero efficitur, ut facilisis lectus convallis. Vivamus sed imperdiet elit, eu dapibus arcu. Morbi eget nisi non nibh dictum aliquam. Etiam nec posuere enim, ac vulputate magna."
      },
      tableItems: [
        {

        }
      ],
      detailItems: {},
      jsonstr: '',
      tableHeaders: [
        {
          text: "My Dataset",
          align: 'start',
          sortable: false,
          value: 'name',
          edditable: true,
        },
        {
          text: "Author",
          align: 'start',
          sortable: false,
          value: 'author',
          edditable: true,
        },
        {
          text: "Information",
          align: 'start',
          sortable: false,
          value: 'information',
          edditable: true,
        },
      ],
      infoField: '',
    };
  },
  filters: {
    pretty: function(value) {
      return value==''? '' :JSON.stringify(value, null, 4);
    }
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
    isInitial() {
        return this.currentStatus === STATUS_INITIAL;
    },
    isSaving() {
      return this.currentStatus === STATUS_SAVING;
    },
    isSuccess() {
      return this.currentStatus === STATUS_SUCCESS;
    },
    isFailed() {
      return this.currentStatus === STATUS_FAILED;
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
    var me = this;
    me.refreshToken();    
    me.init()
  },
  created () {
    this.userID = this.getCookie("userID")
  },
  methods: {
    async init (){
      var params = this.$nuxt.$route.query
      this.dataSetID = params.dataSetID;
      this.getDataSetDetail();
    },

    //
    selectItem(item){
      this.jsonstr = item.item.json
    },
    //
    addDataSet(){
      this.dialog = true
    },

    // Getting data set's detailed data
    async getDataSetDetail(){
      var me = this;
      var dataReq =
      {
        "data_set_id": me.dataSetID,
      };
      me.postToServer(dataReq,me.get_data_set_api).then((res)=>{  
        me.tableItems = res["analyzed"]
        me.detailItems = res["detail"][0]  
        debugger
      })
    },
    async saveData(){
      var me = this
      var dataReq = me.temp
      dataReq.user_id = me.userID
      dataReq.data_set_id = me.dataSetID
      
        
      try {
        dataReq.json = JSON.parse(me.temp.json);
      }
      catch(err) {
        me.swAlert("INPUT","Please enter your data in Json format", "error", ()=>{me.jsonstr=""; return;})
        return;
      } 
      if(me.temp.name == ''){
        me.swAlert("INPUT","Please enter your data's name", "error", ()=>{return})
        return;
      }
      else if(me.temp.description == ''){
        me.swAlert("INPUT","Please enter your data's description", "error", ()=>{return})
        return;
      }
      else if(me.temp.json == ''){
        me.swAlert("INPUT","Please enter your data", "error", ()=>{return})
        return;
      }
      else{
        me.postToServer(dataReq,me.get_data_add_api).then((res)=>{  
          me.dialog= false
          me.getDataSetDetail()
        })
      }
    },
    save(formData) {
      // upload data to the server
      var me = this;
      this.currentStatus = STATUS_SAVING;

      me.upload(formData).then(() => {
        me.uploadedFiles = [];
        me.currentStatus = STATUS_SUCCESS;       
        this.swAlert(this.$t("追加"),this.$t("CSVを追加"),"success", ()=>{ me.addCsvDialog = false; me.getTableData })
        
      })
      .catch(err => {
        me.uploadError = err.response;
        me.currentStatus = STATUS_FAILED;
      });
    },
    filesChange(fieldName, fileList) {
      // handle file changes
      const formData = new FormData();

      if (!fileList.length) return;

      // append the files to FormData
      Array
        .from(Array(fileList.length).keys())
        .map(x => {
          formData.append('file', fileList[x], fileList[x].name);
        });
      formData.append('sub_process_id', this.currentSubProcessID);
      // save it
      this.save(formData);
    },
  }
};
</script>
