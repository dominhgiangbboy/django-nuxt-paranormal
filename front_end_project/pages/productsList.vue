<template>
  <v-container fluid>
    <!-- Add products dialog -->
    <v-dialog
      v-model="productAddDialog"
      max-width="900px"
    >
    
      <v-card class="pa-2">
        <v-card-title class="headline mb-10">
          <span>Add product to project</span>
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Project
                    </div>
                </v-col>
                <v-col>
                   
                    <custom-combo-box
                        label="Project"
                        :comboBoxItems="listProjects"
                        :itemValue="parseInt(projectID)"
                        :disabled="true"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row v-for="(headerItem,index) in tableHeaders" :key="index"  >
              <v-col cols="2" v-if="headerItem.edditable"  class="mt-1"> 
                  <div class="title-text mt-2" style="text-align:end">
                      {{headerItem.text}}
                  </div>
              </v-col> 
              <v-col  v-if="headerItem.edditable"> 
                  <v-text-field
                      v-model="tempItems[headerItem.value]" 
                      type="String"
                      outlined
                      dense
                  >
                  </v-text-field>
              </v-col> 
            </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="darken-1"
            text
            @click="productAddDialog = false"
          >
            Cancel
          </v-btn>
          <custom-button
            v-on:click="addItemProduct"
            label="Add"
          >
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- Add process dialog -->
    <v-dialog
      v-model="processAddDialog"
      max-width="900px"
    >
    
      <v-card class="pa-2">
        <v-card-title class="headline mb-10">
          <span>Add process to product</span>
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Project
                    </div>
                </v-col>
                <v-col>
                   
                    <custom-combo-box
                        label="Project"
                        :comboBoxItems="listProjects"
                        :itemValue="parseInt(projectID)"
                        :disabled="true"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Product
                    </div>
                </v-col>
                <v-col>
                   
                    <custom-combo-box
                        label="Product"
                        :comboBoxItems="tableItems"
                        :itemValue="parseInt(currentProductID)"
                        :disabled="true"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Production plant
                    </div>
                </v-col>
                <v-col>
                    <custom-combo-box
                        label="Choose plant"
                        :comboBoxItems="plantsList"
                        :itemValue="parseInt(plantID)"
                        v-on:change="selectPlant"
                        :rules="rules.required"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row v-for="(headerItem,index) in tableHeaders" :key="index"  >
              <v-col cols="2" v-if="headerItem.edditable"  class="mt-1"> 
                  <div class="title-text mt-2" style="text-align:end">
                      {{headerItem.text}}
                  </div>
              </v-col> 
              <v-col  v-if="headerItem.edditable">
                  <custom-combo-box
                        label="Choose process"
                        :comboBoxItems="listProcessComboBox"
                        :itemValue="parseInt(processDefaultListID)"
                        v-on:change="selectProcessComboBox"
                        :rules="rules.required"
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
            @click="processAddDialog = false"
          >
            Cancel
          </v-btn>
          <custom-button
            v-on:click="itemProcessAdd"
            :disabled="processDefaultListID==0||plantID==0"
            label="Add"
          >
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- edit product dialog -->
    <v-dialog
      v-model="productEditDialog"
      max-width="900px"
    >
    
      <v-card class="pa-2">
        <v-card-title class="headline mb-10">
          <span>Edit product</span>
        </v-card-title>
        <v-card-text>
            <v-row v-for="(headerItem,index) in tableHeaders" :key="index"  >
              <v-col cols="2" v-if="headerItem.edditable"  class="mt-1"> 
                  <div class="title-text mt-2" style="text-align:end">
                      {{headerItem.text}}
                  </div>
              </v-col> 
              <v-col  v-if="headerItem.edditable"> 
                  <v-text-field
                      v-model="editTempItem[headerItem.value]" 
                      type="String"
                      outlined
                      dense
                  >
                  </v-text-field>
              </v-col> 
            </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="darken-1"
            text
            @click="productEditDialog = false"
          >
            Cancel
          </v-btn>
          <custom-button
            v-on:click="itemProductEditAction"
            label="Update"
          >
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!-- edit process dialog -->
    <v-dialog
      v-model="processEditDialog"
      max-width="900px"
    >
    
      <v-card class="pa-2">
        <v-card-title class="headline mb-10">
          <span>Add process to product</span>
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Project
                    </div>
                </v-col>
                <v-col>
                   
                    <custom-combo-box
                        label="Project"
                        :comboBoxItems="listProjects"
                        :itemValue="parseInt(projectID)"
                        :disabled="true"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Product
                    </div>
                </v-col>
                <v-col>
                   
                    <custom-combo-box
                        label="Product"
                        :comboBoxItems="tableItems"
                        :itemValue="parseInt(currentProductID)"
                        :disabled="true"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                    <div class="title-text mt-2" style="text-align:end">
                        Production plant
                    </div>
                </v-col>
                <v-col>
                    <custom-combo-box
                        label="Choose plant"
                        :comboBoxItems="plantsList"
                        :itemValue="parseInt(editTempItem['plant_id'])"
                        v-on:change="selectPlantEdit"
                        :rules="rules.required"
                    >
                    </custom-combo-box>
                </v-col>
            </v-row>
            <v-row v-for="(headerItem,index) in tableHeaders" :key="index"  >
              <v-col cols="2" v-if="headerItem.edditable"  class="mt-1"> 
                  <div class="title-text mt-2" style="text-align:end">
                      {{headerItem.text}}
                  </div>
              </v-col> 
              <v-col  v-if="headerItem.edditable">
                  <custom-combo-box
                        label="Choose process"
                        :comboBoxItems="listProcessComboBox"
                        :itemValue="parseInt(editTempItem['process_type'])"
                        v-on:change="selectProcessEdit"
                        :rules="rules.required"
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
            @click="processEditDialog = false"
          >
            Cancel
          </v-btn>
          <custom-button
            v-on:click="itemProcessEditAction"
            :disabled="editTempItem['process_type']==0||editTempItem['plant_id']==0"
            label="Update"
          >
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
        <v-col :cols="mini?6:3">
            <custom-combo-box
                label="Project"
                :comboBoxItems="listProjects"
                :itemValue="parseInt(projectID)"
                v-on:change="selectProject"
            >
            </custom-combo-box>
        </v-col>
    </v-row>
    <v-row>
      <v-col :cols="mini?12:4">
        <custom-table
            :is-show-all="true"
            :defaultPageSize="10"
            :headerItems="tableHeaders"
            :isLoading="isLoading"
            :dataTableItems="tableItems"
            :singleSelect="true"
            :showSelect="true"
            v-on:selected="selectItems"
            dense
            :isShowAll="true"
            v-on:edit="editItemProduct"
            v-on:delete="deleteItemProduct"
            :isBanner="true"
            v-on:add="addItemProducts"
            :disableAddButton="false"
            height="500"
          >
        </custom-table>
      </v-col>
      <v-col  :cols="mini?12:4">
        <custom-table
            :is-show-all="true"
            :defaultPageSize="10"
            :headerItems="tableHeadersProcess"
            :isLoading="loadingTable2"
            :dataTableItems="process_items"
            noDataText="There is no data here please choose one value"
            dense
            v-on:edit="editItemProcess"
            v-on:delete="deleteItemProcess"
            :isBanner="true"
            v-on:add="addItemProcess"
            :disableAddButton="currentProductID== 0?true:false"
            height="500"
          >
        </custom-table>
      </v-col>
    </v-row>
  </v-container>
</template>
<style lang="scss" scoped>
 
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
</style>
<script>

export default {
  data() {
    return {
      productAddDialog: false,
      productDialog: false,
      isLoading: false,
      showUpdate:false,
      comboBoxItems: [],
      infoField: '',
      deleteDialog: false,
      tableHeaders: [
        {
          text: '案件名',
          align: 'start',
          sortable: false,
          value: 'name',
          edditable: true,
        },
        {
          text: '',
          align: 'start',
          sortable: false,
          width: 100,
          value: 'input',
        },
        
      ],
      tableHeadersProcess: [
        {
          text: '大工程',
          align: 'start',
          sortable: false,
          value: 'name',
          edditable: true,
        },
        {
          text: '原価表名',
          align: 'start',
          sortable: false,
          value: 'plant_name',
        },
        
        {
          text: '',
          align: 'start',
          sortable: false,
          width: 100,
          value: 'input',
        },
        
      ],
      loadingTable2:false,
      tableItems:[
      ],
      tempItems: { 
        "name": "",
        "project_id": 0,
      },
      tempItemsProcess: { 
        "name": "",
        "project_id": 0,
        "product_id": 0,
        "plant_id":   0,
      },
      rules:[
        {required: value => !!value || 'This infomation is required'}
      ],
      process_items: [],
      current_delete_id: 0,
      selectedItems:[],
      currentProductID: 0,
      plantsList: [],
      projectID:  0,
      plantID: 0,
      processDefaultListID:0,
      listProjects: [],
      listProcessComboBox:[],
      //process dialog
      processAddDialog: false,
      processEditDialog: false,
      //product dialog
      productEditDialog: false,
      productAddDialog: false,

      editTempItem: {},
      deleteTableTempID:0,
      deleteTableTempApi:"",
      // API link
      get_products_api :"get-products-list/",
      update_products_api :"update-products-detail/",
      update_process_api :"update-process-detail/",
      get_projects_api :"get-projects-list/",
      delete_products_api :"delete-products-list/",
      add_products_api :"add-products-list/",
      get_processes_api :"get-process-detail/",
      add_processes_api :"add-process-detail/",
      get_processes_plant_api :"get-process-plant/",
      get_plant_api :"index/get-plant-list/",
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
      var params = this.$nuxt.$route.query
      this.projectID = params.projectID;
      this.$nuxt.$on('insertClick', () => {
        //this.insertClick();
      })
      
      me.refreshToken();
      me.dataTableGet();
      me.getProjects();
      me.getPlantsList();
      me.configButton('update',true, true)
      me.configButton('delete', true, true)
      me.selectedItems.push(me.tableItems[0])
    },
    async clickButton () {
      
    },
    deleteDialogOpen(item){
      this.deleteDialog = true;

      this.current_delete_id = item.item.id
    },
    // Add to product list
    async addItemProduct(){
      var me = this;
      var dataReq = me.tempItems
      dataReq["project_id"] = parseInt(me.projectID)
      me.postToServer(dataReq,me.add_products_api).then((res)=>{
        
        me.productAddDialog = false;
        me.dataTableGet()
        me.tempItems = {
          "name": "",
        }
      })
    },
    
    // Get combo box items
    async dataTableGet(){
      var me = this;
      var dataReq;
      this.isLoading = true;
      if(me.productID != 0){
        dataReq = {
            "project_id": me.projectID
        }
      }
      me.postToServer(dataReq,me.get_products_api).then((res)=>{
        me.tableItems = res
        this.isLoading = false;
      })
    },
    async getPlantsList(){
      var me = this;
      var dataReq;
      me.postToServer(dataReq,me.get_plant_api).then((res)=>{  
        me.plantsList = res
      })
    },
    // get process by plant ID
    async getProcessByPlant(plant_id){
      var me = this;
      var dataReq;
      if(plant_id != 0){
        dataReq= 
        {
          "plant_id": plant_id,
          "product_id": me.currentProductID,
          "project_id": me.projectID,
          "process_type": me.editTempItem['process_type'],
        }
      }
      me.postToServer(dataReq,me.get_processes_plant_api).then((res)=>{  
        me.listProcessComboBox = res
      })
    },
    // Get combo box items
    async getProjects(){
      var me = this;
      var dataReq;
      if(me.productID != 0){
        dataReq = {
            "project_id": me.projectID
        }
      }
      me.postToServer(dataReq,me.get_projects_api).then((res)=>{
          me.listProjects = res
      })
    },
    async getProcessTableData(productId){
      var me = this
      var dataReq;
      me.loadingTable2 = true;
      dataReq = {
        "product_id": productId,
      }
      me.currentProductID = productId
      me.postToServer(dataReq,me.get_processes_api).then((res)=>{
        me.process_items = res
        me.loadingTable2 = false;
      })
    },
    selectItems(item){
      var me = this;
      
      if(item.value){
        var productId =  item.item.id
        me.currentProductID =  item.item.id;
        me.getProcessTableData(productId)
        
      }
      else if (!item.value){
        if(item.item.id == me.currentProductID){
          me.currentProductID = 0;
          me.process_items = [];
        }
      }
    },
    deleteItemFromTable(){
      var me = this;
      if(me.deleteTableTempID != 0){
        var dataReq;
        dataReq = {
          "id":me.deleteTableTempID
        }
        me.postToServer(dataReq,me.deleteTableTempApi).then((res)=>{
          if(me.deleteTableTempApi == "delete-process-detail/"){
            me.processDefaultListID = 0
            me.plantID = 0
            me.getProcessTableData(me.currentProductID);
            me.getProcessByPlant(me.plantID);
          }
          else if(me.deleteTableTempApi == me.delete_products_api){
            me.processDefaultListID = 0
            me.plantID = 0
            me.currentProductID = 0
            me.process_items = []
            me.dataTableGet();
          }
        })
      }
    },
    deleteItemProduct(item){
      //open delete dialog
      this.deleteTableTempID = item.item.id
      this.deleteTableTempApi = this.delete_products_api
      this.swAlert("Delete","Delete product?","warning", this.deleteItemFromTable)
    },
    deleteItemProcess(item){
      //open delete dialog
      this.deleteTableTempID = item.item.id
      this.deleteTableTempApi = "delete-process-detail/"
      this.swAlert("Delete","Delete process?","warning", this.deleteItemFromTable)
    },
    editItemProduct(item){
      this.editTempItem = item.item
      this.productEditDialog = true;
    },
    editItemProcess(item){
      this.editTempItem = item.item
      this.getProcessByPlant(this.editTempItem["plant_id"])
      this.processEditDialog = true;
    },
    addItemProducts(item){
      this.productAddDialog = true;
    },
    addItemProcess(){
      this.processAddDialog = true;
    },
    async itemProductEditAction(item){
      var me = this;
      var dataReq = me.editTempItem
      me.postToServer(dataReq,me.update_products_api).then((res)=>{
        me.productEditDialog = false;
        me.dataTableGet()
      })
    },
    async itemProcessEditAction(item){
      var me = this;
      var dataReq = me.editTempItem
      me.postToServer(dataReq,me.update_process_api).then((res)=>{
        me.processEditDialog = false;
        me.getProcessTableData(me.currentProductID)
      })
    },
    
    itemProcessAdd(){
      var me = this;
      if(me.plantID != 0){
        var dataReq;
        dataReq = {
          "product_id":me.currentProductID,
          "process_type": me.processDefaultListID,
          "plant_id": me.plantID,
          "project_id": me.projectID,
        }
        me.postToServer(dataReq,me.add_processes_api).then((res)=>{
          me.plantID = 0
          me.processDefaultListID = 0;
          me.getProcessTableData(me.currentProductID);
          me.getProcessByPlant(me.plantID);
          
          me.processAddDialog = false
        })
      }
    },

    selectPlantEdit(plant_id){
      this.editTempItem["plant_id"] = plant_id
      this.editTempItem["process_type"]  = 0
      this.getProcessByPlant(plant_id);
    },
    selectPlant(plant_id){
      this.plantID = plant_id
      this.processDefaultListID  = 0
      this.getProcessByPlant(plant_id);
    },
    selectProcessEdit(process_id){
      this.editTempItem["process_type"]  = process_id
    },
    selectProcessComboBox(process_id){
      this.processDefaultListID = process_id
    },
    selectProject(project_id){
      this.projectID = project_id
      this.currentProductID = 0
      this.process_items = []
      this.dataTableGet();
    },
    clear() {
      this.$refs.form.reset();
    },
    // Created chart function
    
  }
};
</script>
        
  
    
   

