<template>
  <v-container class="container" fluid>
    <v-dialog
      v-model="dialog"
      max-width="500px"
    >
      <v-card class="pa-2">
        <v-card-title class="mb-5 dialog-header-text" >
          原価表の追加
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="mt-5">
          <v-row>
            <v-col cols="3">
              <div class="header-text">
                工程名
              </div>
            </v-col>
            <v-col>
                <v-text-field outlined dense>
                </v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col  cols="3">
              <div class="header-text">
                工場
              </div>
            </v-col>
            <v-col>
                <custom-combo-box>
                </custom-combo-box>
            </v-col>
          </v-row>
          <v-row>
            <v-col  cols="3">
              <div class="header-text">
                予算の項目
              </div>
            </v-col>
            <v-col>
                <custom-combo-box>
                </custom-combo-box>
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
          <custom-button label="Update" v-on:click="dialog= false">
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-card
      outlined 
      class="mt-10 pa-10"
    >
      <v-row>
        <v-col :cols="mini ? 2 :1"
        class="anken">
          <div>
            案件
          </div>
        </v-col>
        <v-col :cols="mini ? 7 : 3">
          <custom-combo-box label="案件" :comboBoxItems="project_items" v-on:change="itemComboChangeProjects">
          </custom-combo-box>
        </v-col>
        <v-col cols="2"></v-col>
        <!-- <v-col :cols="mini ? 2 :1"
        class="jikan">
          <div>時間</div>
        </v-col>
        <v-col :cols="mini ? 7 : 3">
          <v-menu
            v-model="menu2"
            :close-on-content-click="false"
            transition="slide-x-transition"
            bottom
            min-width="auto"
            
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date"
                append-icon1="mdi-calendar"
                outlined
                v-bind="attrs"
                v-on="on"
                dense
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
          </v-menu>
        </v-col> -->
      </v-row>
      <v-row
      >
        <v-col :cols="mini ? 2 :1"
          class="koutei">
          <div>
            原価表
          </div>
        </v-col>
        <v-col :cols="mini ? 7 : 3">
          <custom-combo-box label="原価表" :comboBoxItems="product_items" v-on:change="itemComboChangeProducts">
          </custom-combo-box>
        </v-col>
        <v-col cols="2">
          <custom-button label="原価表の追加" v-on:click="dialog= true"  >
          </custom-button>
        </v-col>
      </v-row>
    </v-card>
    <v-row class="pt-10">
      <v-col>
        <!-- Main Table -->
        <custom-table
          :is-show-all="true"
          :defaultPageSize="10"
          :headerItems="tableHeaders"
          :isLoading="isLoading"
          :dataTableItems="tableItems"
          v-on:openlink = "openLink"
        >
        </custom-table>
      </v-col>
    </v-row>
    <v-card
      outlined 
      class="mt-10 pl-10 pr-10 pb-10"
    >
      <v-card-title>合算</v-card-title>
      <v-row>
        <v-col :cols="mini?12:4">
          <custom-button label="合算" :isBlock="mini?true:true" :isLink="true" link="masterLayouts/insertBudget">
          </custom-button>
        </v-col>
        <v-col  :cols="mini?12:4">
          <custom-button label="合算の 集計結果１" :isBlock="mini?true:true" :isLink="true" link="masterLayouts/totalCost">
          </custom-button>
        </v-col>
        <v-col  :cols="mini?12:4">
          <custom-button :label="'合算の 集計結果２'" :isBlock="mini?true:true" :isLink="true" link="masterLayouts/otherCalculations">
          </custom-button>
        </v-col>
      </v-row>
    </v-card>  
  </v-container>
</template>
<style lang="scss" scoped>
.container {
  padding: 2rem;
}
.icon-button{
    width: 40px  !important;
     height: 40px  !important;
     background-color: #2C73D2 !important;
}
.text-header{
  color: whitesmoke  !important;
  text-align: center !important; 
  background-color: #2C73D2 !important;
}
.main-button{
    background-color: #2C73D2 !important;
    color: whitesmoke  !important;
}
.header{
  font-weight: bold ;
  font-size: 20px;
}
.anken{
    font-weight: bold;
    font-size: 20px;
    text-align: right;
}
.koutei{
    font-weight: bold;
    font-size: 20px;
    text-align: right;
}
.jikan{
    font-weight: bold;
    font-size: 20px;
    text-align: right;}
.addkoutei{
    font-weight: bold;
    font-size: 20px;
    text-align: center; 
    padding-top: 30px;
}
.inserttext{
    padding-left: 8px !important; 
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
      isLoading: false,
      tableHeaders: [
        {
          text: '案件名',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        {
          text: '原価表名',
          align: 'start',
          sortable: false,
          value: 'project_name',
        },
        {
          text: '',
          align: 'start',
          sortable: false,
          value: 'actions',
        },
        
      ],
      tableItems:[
        {
          name: 'Giang',
          project_name: 'Test',
        }
      ],
      dialog: false,
      search: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      get_projects_api: 'get-projects-list/',
      get_products_api: 'get-products-list/',
      current_project_id: 0,
      current_product_id: 0,
      //
      project_items: [],
      product_items: [],
      select: ["案件"],
      items: ["案件A", "案件B", "案件C"],
      headers: [
        {
          text: "鉄骨工事予算実行原価表",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: '工事項目', value: '' },
      ],

      鉄骨工事予算実行原価表: [
       
        
        
      ],
    };
  },
  methods: {
    init(){
      var me = this;
      me.refreshToken();
      me.configButton('update',false, false)
      me.configButton('delete', false, false)
      me.mainTableGet();
      me.getListProjects();
      me.getListProducts();
      
    },
    // change product combo-box
    itemComboChangeProducts(idItem){
      this.current_product_id = idItem
    },
    //change project combo-box
    itemComboChangeProjects(idItem){
      this.current_project_id = idItem
      this.mainTableGet()
    },
      // Get combo box items
    async getListProjects(){
      var me = this;
      var dataReq;
      me.postToServer('',me.get_projects_api).then((res)=>{
        me.project_items= res
      })
    },
     // Get combo box items
    async getListProducts(){
      var me = this;
      
      me.postToServer('',me.get_products_api).then((res)=>{
        me.product_items= res
      })
    },
    // Get combo box items
    async mainTableGet(){
      var me = this;
      var dataReq;
      if(me.current_project_id != 0){
          dataReq = {
            'project_id':me.current_project_id 
          }
      }
      me.postToServer(dataReq,me.get_products_api).then((res)=>{
        me.tableItems= res
      })
    },
    submit() {      
    },
    buttonclick1(){ 
      
    },
    openLink(item, id){
      var me = this;
      switch(id){
        case 1:
          me.$nuxt.$router.push({ path: '/masterLayouts/insertBudget', query: { productID: item.id } })
          break
        case 2:
          me.$nuxt.$router.push({ path: '/masterLayouts/totalCost', query: { productID: item.id } })
          break
        case 3:
          me.$nuxt.$router.push({ path: '/masterLayouts/otherCalculations', query: { productID: item.id } })
          break
        default:
          break
      }
    },
    clear() {
      this.$refs.form.reset();
    },
  },
};
</script>
