<template>
  <v-container fluid>
    <!-- add dialog -->
    <v-dialog
      v-model="addDialog"
      max-width="900px"
    >
      <v-card class="pa-2">
        <v-card-title class="headline mb-5">
          <span>Add Project</span>
        </v-card-title>
        <v-card-text>
            <v-row v-for="(headerItem,index) in tableHeaders" :key="index"  >
              <v-col cols="2" v-if="headerItem.edditable"  class="mt-1"> 
                  <div>
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
        <v-col cols="4">
          <custom-button
            v-on:click="addItem"
            label="My analyzed data"
            :isBlock="true"
          >
          </custom-button>
        </v-col >
          
        <v-col cols="4">
          <custom-button
            v-on:click="addItem"
            label="Upload new analyzed data"
            :isBlock="true"
          >
          </custom-button>
        </v-col>
          
        <v-col cols="4">
          <custom-button
            v-on:click="addItem"
            label="Get data set"
            :isBlock="true"
          >
          </custom-button>
        </v-col>

        <v-col cols="4">
          <custom-button
            v-on:click="addItem"
            label="Pre-processed data"
            :isBlock="true"
          >
          </custom-button>
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
      addDialog: false,
      isLoading: false,
      showUpdate:false,
      editDialog:false,
      comboBoxItems: [],
      infoField: '',
      deleteDialog: false,
      tempItemsEdit:{},
      tableHeaders: [
        {
          text: '案件名',
          align: 'start',
          sortable: false,
          value: 'name',
          edditable: true,
        },
        {
          text: '工事名',
          align: 'start',
          sortable: false,
          value: '工事名',
          edditable: true,
        },
        {
          text: '契約金額',
          align: 'start',
          sortable: false,
          value: '契約金額',
          edditable: true,
        },
        {
          text: '材料費',
          align: 'start',
          sortable: false,
          value: '材料費',
          edditable: true,
        },
        {
          text: '外注費',
          align: 'start',
          sortable: false,
          value: '外注費',
          edditable: true,
        },
        {
          text: '付加価値額',
          align: 'start',
          sortable: false,
          value: '付加価値額',
          edditable: true,
        },
        {
          text: '',
          align: 'start',
          sortable: false,
          width: 100,
          value: 'input',
        },
        {
          text: '',
          align: 'center',
          width: 20,
          sortable: false,
          value: 'actions',
        }
        
      ],
      tableItems:[
        {
          name: 'Giang',
          原価表名: 'Test',
        }
      ],
      tempItems: { 
        "name": "",
        "年間必要固定費額": "",
        "月間必要固定費額": "",
        "一日当り必要固定費額": "",
        "一日当り付加価値額収支": "",
        "総付加価値額": ""
      },
      current_delete_id: 0,
      get_projects_api :"get-projects-list/",
      delete_projects_api :"delete-projects-list/",
      add_projects_api :"add-projects-list/",
      update_projects_api :"update-projects-list/",
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
      me.refreshToken();
      me.dataTableGet();
      me.configButton('update',true, true)
      me.configButton('delete', true, true)
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
      me.postToServer(dataReq,me.add_projects_api).then((res)=>{
        me.addDialog = false;
        me.dataTableGet()
        me.tempItems = {
          "name": "",
          "年間必要固定費額": "",
          "月間必要固定費額": "",
          "一日当り必要固定費額": "",
          "一日当り付加価値額収支": "",
          "総付加価値額": ""
        }
      })
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
      me.postToServer(dataReq,me.get_projects_api).then((res)=>{
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
