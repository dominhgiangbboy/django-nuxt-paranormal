<template>
  <v-container class="container" fluid>
    <!-- add Plant dialog -->
    <v-dialog
      v-model="addDialog"
      max-width="900px"
    >
      <v-card class="pa-2">
        <v-card-title class="headline mb-5">
          <span>Add {{addTitle}}</span>
        </v-card-title>
        <v-card-text>
            <v-row v-for="(headerItem,index) in tempHeaderItems" :key="index"  >
              <v-col cols="2" v-if="headerItem.edditable"  class="mt-1"> 
                  <div>
                      {{headerItem.text}}
                  </div>
              </v-col> 
              <v-col  v-if="headerItem.edditable"> 
                  <v-text-field
                      v-model="tempAddItems[headerItem.value]" 
                      type="String"
                      outlined
                      dense
                  >
                  </v-text-field>
              </v-col>
              <v-col cols="2" v-if="headerItem.isCombobox"  class="mt-1"> 
                    <div>
                        {{headerItem.text}}
                    </div>
                </v-col> 
                <v-col  v-if="headerItem.isCombobox"> 
                    <custom-combo-box
                    :label="headerItem.text"
                    :comboBoxItems="tableItemsTemp[headerItem.text + 'data']"
                    :itemValue="parseInt(defaultCombo[headerItem.text])"
                    v-on:change="selectCombobox"
                    >
                    </custom-combo-box>
                </v-col> 
            </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="darken-1"
            text
            @click="addDialog = false"
          >
            Cancel
          </v-btn>
          <custom-button
            v-on:click="addItem"
            label="Add"
          >
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
   
      <v-row>
        <v-col  :cols="mini?'6':'3'">
          <custom-combo-box
            label="Choose category"
          >
          </custom-combo-box>
        </v-col>
        <v-col  :cols="mini?'6':'3'">
          <custom-combo-box
            label="Choose data set"
          >
          </custom-combo-box>
        </v-col>
        <v-col  :cols="mini?'6':'3'">
          <custom-combo-box
            label="Choose source"
          >
          </custom-combo-box>
        </v-col>
        <v-col  :cols="mini?'6':'3'">
          <custom-button
            v-on:click="addItem"
            label="Search"
          >
          </custom-button>
        </v-col>
      </v-row>
  
    
      <v-row>
        <v-col>
          <custom-table
                :defaultPageSize="10"
                :headerItems="tableHeaders"
                :isLoading="isLoading"
                :dataTableItems="tableItems"
                :singleSelect="true"
                dense
                :isShowAll="false"
                v-on:edit="editItemPlant"
                v-on:delete="deleteItemPlant"
                :isBanner="true"
                v-on:add="addItemPlant"
                toobarTitle="Data set list"
                :disableAddButton="false"
                height="500"
            >
          </custom-table>
        </v-col>        
    </v-row>

  </v-container>
</template>
<style lang="scss" scoped>
    .mb-20{
      margin-bottom: 4rem;   
    }
    .tab-item{
      padding: 1rem;
    }
    .combobox-header{
        text-align: right;
        font-weight: bold;
    }
    .combobox-header-left{
        text-align: left;
        font-weight: bold;
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
  },
  mounted(){
    // get default value
    this.init();
  },
  data() {
    return {
      // Plant data
      tableHeaders: [
        {
          text: "Dataset's name",
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
        {
          text: "Feature",
          align: 'start',
          sortable: false,
          value: 'feature',
          edditable: true,
        },
        {
          text: '',
          align: 'start',
          sortable: false,
          width: 400,
          value: 'actions',
        },
      ],
     
      tableItems: [
        {
          name: "Running data set",
          author: "BK's students",
          information: "Created with crawled data from the internet"
        }
      ],  
      plantAddDialog: false,
      currentPlantID : 0,
      isLoadingPlant: false,
      tableItemsPlantProcess:  [],
      tableAllItemsSubProcess: [],
      isLoadingPlantProcess:false,
      tableItemsProcess: [],  
      ProcessAddDialog: false,
      currentProcessID : 0,
      isLoadingProcess: false,
      // SUb process
      tableItemsSubProcess : [],
     
      //
      action: 0,
      currentItem:0,
      tab: null,
      isLoading: false,
      dialog: false,
      search: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      status: false,
      //API link 
      get_plant_api :"index/get-plant-list/",
      get_data_set_api :"data-set-get/",
      add_plant_item:"index/add-plant-list/",
      update_plant_item:"index/update-plant-list/",
      delete_plant_item: "index/delete-plant-list/",
      add_process_item: "index/add-process-list/",
      delete_process_item: "index/delete-process-list/",
      update_process_item: "index/update-process-list/",
      get_sub_process_api: "index/get-sub-process-list/",
      delete_sub_process_api: "index/delete-sub-process-list/",
      add_sub_process_api: "index/add-sub-process-list/",
      update_sub_process_api: "index/update-sub-process-list/",
    };
  },
  methods: {
    init(){
      this.refreshToken();
    },
    async getDataSetItems(){
      var me = this;
      var dataReq =
      {
      };
      me.postToServer(dataReq,me.get_data_set_api).then((res)=>{  
        me.tableItemsPlantProcess = res
      })
    },
    // plant actions
    async getPlantsList(){
      var me = this;
      var dataReq;
      me.postToServer(dataReq,me.get_plant_api).then((res)=>{  
        me.tableItemsPlant = res
      })
    },
    selectItemsPlant(item){
        var me = this;    
        if(item.value){
            var plantID =  item.item.id
            me.currentPlantID = item.item.id
            me.getPlantProcessItems()
        }
        else if (!item.value){
            if(item.item.id == me.currentPlantID){
                me.currentPlantID = 0;
                me.process_items = [];
            }
        }
    },
    editItemPlant(item){
        this.tempAPIUrl = this.update_plant_item
        this.tempHeaderItems = this.tableHeadersPlant
        this.tempAddItems = item.item
        this.addDialog = true
    },
    addItemPlant(){
        this.action = 1
        
        this.tempAPIUrl = this.add_plant_item
        this.tempHeaderItems = this.tableHeadersPlant
        this.addDialog = true
    },
    deleteItemPlant(item){
      //open delete dialog
      this.deleteTableTempID = item.item.id
      this.deleteTableTempApi = this.delete_plant_item
      this.swAlert("Delete","Delete plant?","warning", this.deleteItemFromTable)
    },
    // Process actions
    async getProcesssList(){
      var me = this;
      var dataReq;
      me.postToServer(dataReq,me.get_plant_process_api).then((res)=>{  
        me.tableItemsProcess = res
      })
    },
    selectItemsProcess(item){
        var me = this;    
        if(item.value){
            var ProcessID =  item.item.id
            me.currentProcessID = item.item.id
            me.getSubProcessItems(me.currentProcessID)
            me.getSubProcessItems(0,me.currentProcessID)
        }
        else if (!item.value){
            if(item.item.id == me.currentProcessID){
                me.currentProcessID = 0;
                me.tableItemsSubProcess = [];
            }
        }
    },
    editItemProcess(item){
        this.currentItem = 1
        this.tempAPIUrl = this.update_process_item
        this.tempHeaderItems = this.tableHeadersProcess
        this.tableItemsTemp["工場data"] = this.tableItemsPlant
        this.tempAddItems = item.item
        this.defaultCombo["工場"] = 1
        this.addDialog = true
    },
    addItemProcess(){
        this.currentItem = 1
        this.action = 1
        this.tempAddItems = {}
        this.defaultCombo["工場"] = 1
        this.tempAddItems["plant_id"] = 1
        this.tableItemsTemp["工場data"] = this.tableItemsPlant
        this.tempAPIUrl = this.add_process_item
        this.tempHeaderItems = this.tableHeadersProcess
        this.addDialog = true
    },
    deleteItemProcess(item){
      //open delete dialog
      this.deleteTableTempID = item.item.id
      this.deleteTableTempApi = this.delete_process_item
      this.swAlert("Delete","Delete Process?","warning", this.deleteItemFromTable)
    },
    // SUb process
    async getSubProcessItems(id_process, process_id){
      var me = this;
      var dataReq;
      if(id_process != null && id_process != 0){
          dataReq ={
              "id_process": id_process
          }
           me.postToServer(dataReq,me.get_sub_process_api).then((res)=>{  
                me.tableItemsSubProcess = res
            })
      }
      else if(process_id != null && process_id != 0){
          dataReq ={
              "process_id": process_id
          }
           me.postToServer(dataReq,me.get_sub_process_api).then((res)=>{  
        
                me.tableComboboxSubProcess = res
           })
      }
      else{
        me.postToServer(dataReq,me.get_sub_process_api).then((res)=>{  
                me.tableAllItemsSubProcess = res
        })
      }
     
    },
    editSubProcess(item){
        this.currentItem = 2
        this.action = 2
        this.tempAPIUrl = this.update_sub_process_api
        this.tempHeaderItems = this.tableHeadersSubProcess
        this.tableItemsTemp["Subdata"] = this.tableComboboxSubProcess
        this.tempAddItems = item.item
        this.currentTempID = item.item.id
        this.defaultCombo["id"] = 1
        this.addDialog = true

    },
    addSubProcess(){
        this.currentItem = 2
        this.action = 2
        this.tempAddItems = {}
        this.defaultCombo["id"] = 1
        this.tempAddItems["id"] = 1
        this.tableItemsTemp["Subdata"] = this.tableComboboxSubProcess
        this.tempAPIUrl = this.add_sub_process_api
        this.tempHeaderItems = this.tableHeadersSubProcess
        this.addDialog = true
    },
    addSubProcessAll(){
        this.action = 1
        this.tempAddItems = {}
        this.tempAPIUrl = this.add_sub_process_api
        this.tempHeaderItems = this.tableHeadersAllSubProcess
        this.addDialog = true
    },
    editSubProcessAll(item){
        this.action = 1
        this.tempAddItems = item.item
        this.tempAPIUrl = this.update_sub_process_api
        this.tempHeaderItems = this.tableHeadersAllSubProcess
        this.addDialog = true
    },
    deleteSubProcess(item){
        //open delete dialog
      this.deleteTableTempID = item.item.id
      this.deleteTableTempApi = this.delete_sub_process_api
      this.swAlert("Remove from process","Remove sub Process?","warning", this.removeProcess)
    },

     deleteSubProcessAll(item){
        //open delete dialog
      this.deleteTableTempID = item.item.id
      this.deleteTableTempApi = this.delete_sub_process_api
      this.swAlert("Remove from process","Remove sub Process?","warning", this.deleteItemFromTable)
    },
    removeProcess(){
        var me = this;
        if(me.deleteTableTempID != 0){
            var dataReq;
            dataReq = {
              "id":me.deleteTableTempID,
              "id_process": me.currentProcessID,
            }
            me.postToServer(dataReq, me.deleteTableTempApi).then((res)=>{
                me.getSubProcessItems(me.currentProcessID)
            })
        }
    },
    selectCombobox(id){
       var me = this
       if(this.currentItem == 1){
           this.tempAddItems["plant_id"] = id
       }
       if(this.currentItem == 2){
           this.tempAddItems["id"] = id
       }
    },
    deleteItemFromTable(){
        var me = this;
        if(me.deleteTableTempID != 0){
            var dataReq;
            dataReq = {
              "id":me.deleteTableTempID
            }
            me.postToServer(dataReq, me.deleteTableTempApi).then((res)=>{
                if(me.deleteTableTempApi ==  me.delete_plant_item){
                    me.getPlantsList()
                }
                else if(me.deleteTableTempApi ==  me.delete_process_item){
                    me.getProcesssList()
                }
                else if(me.deleteTableTempApi ==  me.delete_sub_process_api){
                    me.getSubProcessItems()
                }
            })
        }
    },
    addItem(){
        var me = this;
        var dataReq = me.tempAddItems;
        me.status = false;
        if(me.action == 2){
            dataReq["process_id"] = me.currentProcessID
            dataReq["current_id"] = me.currentTempID
        } 
        me.tempHeaderItems.forEach(header => {
            if(header.edditable){
                if(me.tempAddItems[header.value] =="" ||me.tempAddItems[header.value] == null ||me.tempAddItems[header.value] == undefined){
                    me.status = true
                    this.swAlert("Insert value","Please input value to " + header.text,"warning", me.submit)
                    return;
                }   
            }
        });
        if(!me.status){
            me.postToServer(dataReq,me.tempAPIUrl).then((res)=>{  
            if(me.tempAPIUrl ==  me.add_plant_item ||me.tempAPIUrl ==  me.update_plant_item){
                me.getPlantsList()
                me.addDialog = false
            }
            else if(me.tempAPIUrl ==  me.add_process_item ||me.tempAPIUrl ==  me.update_process_item){
                me.getProcesssList()
                me.addDialog = false
            }
            else if(me.tempAPIUrl ==  me.add_sub_process_api ||me.tempAPIUrl ==  me.update_sub_process_api){
                me.getSubProcessItems(me.currentProcessID)
                me.getSubProcessItems(0,me.currentProcessID)
                me.getSubProcessItems(0,0)
                me.addDialog = false
            }
            })
        }
        
    },
    submit() {      
        return "";
    },
    buttonclick1(){ 
      
    },
    clear() {
      this.$refs.form.reset();
    },
  },
};
</script>
