<template>
  <v-container class="container" fluid>
    <v-dialog
      v-model="dialog"
      max-width="500px"
    >
      <v-card class="pa-2">
        <v-card-title class="mb-5 dialog-header-text" >
          工程追加
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
                <v-text-field outlined dense >
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
    <v-card outlined>
      <v-tabs
        v-model="tab"
        background-color="#1d3557"
        class="tab-bar"
        dark
      >
        <v-tab>
          Summary
        </v-tab>
        <v-tab>
          Detailed table
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
      <v-tab-item  
        class="tab-item"
      >
      
       <v-row>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['工事番号']"
              label-header="工事番号"
              v-on:input="change_product_info"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['用途']"
              label-header="用途"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['工事項目']"
              label-header="工事項目"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['工事名']"
              label-header="工事名"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['記録日']"
              label-header="記録日"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['記録日']"
              label-header="設計事務所"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['総付加価値額']"
              label-header="総付加価値額"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['得意先']"
              label-header="得意先"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['設計事務所']"
              label-header="設計事務所"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              :textField="product_info['構造_規模_延床']"
              label-header="構造・規模・延床"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="亜鉛メッキ部ｔｏｎ数"
              :textField="product_info['総ton数']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="総ｔｏｎ数"
              :textField="product_info['総ton数']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="建方予定日"
              :textField="product_info['建方予定日']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="工事担当者"
              :textField="product_info['工事担当者']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="営業担当者"
              :textField="product_info['営業担当者']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="予算決定者"
              :textField="product_info['予算決定者']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="記録者"
              :textField="product_info['記録者']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="見積金額"
              :textField="product_info['見積金額']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="契約金額"
              :textField="product_info['契約金額']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="フロッヒーNO"
              :textField ="product_info['フロッヒーNO']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="受注時値引率"
              :textField ="product_info['受注時値引率']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:3">
            <custom-info-field
              label-header="備考"
              :textField ="product_info['備考']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:6">
            <custom-info-field
              label-header="裏当金_ピース_ブレースシート等"
              :textField ="product_info['裏当金_ピース_ブレースシート等']"
            ></custom-info-field>
          </v-col>
          <v-col :cols="mini?6:6">
              <div class="pl-2 text-red">
                全材料購入重量: {{product_info['全材料購入重量']}} t
              </div>
              <div class="pl-2 text-red">
                全材料購入単価: {{product_info['全材料購入単価']}}　円/ton 
              </div>
          </v-col>
        </v-row>
      </v-tab-item>
       <v-tab-item class="tab-item"
      >
        <v-row>
        <v-col>
          <!-- Main Table -->
          <custom-table
            :is-show-all="true"
            :defaultPageSize="10"
            :headerItems="tableHeaders"
            :isLoading="isLoading"
            :dataTableItems="tableItems"
            v-on:saveItem="saveItem"
          >
          </custom-table>
        </v-col>
      </v-row>
      </v-tab-item>
    </v-tabs-items>
    </v-card>
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
      tableHeaders: [
        {
          text: '項目',
          align: 'start',
          sortable: false,
          edditable: false,
          value: 'name',
        },
        {
          text: 'ｔｏｎ当り営業予算金額      円/ｔｏｎ',
          align: 'start',
          sortable: false,
          edditable: false,
          value: '営業予算金額_calculated',
        },
        {
          text: '営業予算金額',
          align: 'start',
          edditable: true,
          sortable: false,
          value: '営業予算金額',
        },
        {
          text: 'ｔｏｎ当り実行予算金額      円/ｔｏｎ',
          align: 'start',
          sortable: false,
          edditable: false,
          value: '実行予算金額_calculated',
        },
        {
          text: '実行予算金額',
          align: 'start',
          sortable: false,
          edditable: true,
          value: '実行予算金額',
        },
        {
          text: 'ｔｏｎ当り実行原価金額       円/ｔｏｎ',
          align: 'start',
          sortable: false,
          edditable: false,
          value: '実行原価金額_calculated',
        },
        {
          text: '実行原価金額',
          align: 'start',
          sortable: false,
          edditable: true,
          value: '実行原価金額',
        },
        {
          text: '実行予算対原価差異',
          align: 'start',
          sortable: false,
          edditable: false,
          value: '実行原価金額_calculated',
        },
        {
          text: '構成比',
          align: 'start',
          sortable: false,
          edditable: false,
          value: '構成比_calculated',
        },
        {
          text: 'input',
          align: 'start',
          edditable: false,
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
      product_info: [],
      dialog: false,
      search: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      select: ["案件"],
      items: ["案件A", "案件B", "案件C"],
      productID: 0,
      get_detail_cost_api: 'get-table-cost/',
      get_product_detail_api: 'get-products-detail/',
      update_detail_cost_api: 'update-table-cost/'
    };
  },
  mounted(){
    this.init();
    
  },
  methods: {
    init(){
      var params = this.$nuxt.$route.query
      this.productID = params.productID;
      if(this.tableItems.length > 0){
        this.isLoading = false
      }
      this.datatableItem();
      this.getCommonInfo();
    },
    async saveItem(item){
      var me = this;
      var dataReq = []
      item.営業予算金額 = parseFloat(item.営業予算金額)
      item.実行予算金額 = parseFloat(item.実行予算金額)
      item.実行原価金額 = parseFloat(item.実行原価金額)
      dataReq.push(item)
      me.postToServer(dataReq,me.update_detail_cost_api).then((res)=>{
        me.tableItems= res
        this.datatableItem();
      })
      
    },
    // get Common info
    async getCommonInfo(){
      var me = this;
      var dataReq;
      if(me.productID != 0){
          dataReq = {
            'id':me.productID 
          }
      }
      me.postToServer(dataReq,me.get_product_detail_api).then((res)=>{
        console.log(res)
        me.product_info= res[0]
        console.log(me.product_info['工事番号'])
      })
    },
    // Get table data
    async datatableItem(){
      var me = this;
      var dataReq;
      if(me.productID != 0){
          dataReq = {
            'product_id':me.productID 
          }
      }
      me.postToServer(dataReq,me.get_detail_cost_api).then((res)=>{
        me.tableItems= res
      })
    },
    change_product_info(value, header){
      switch (header){
        case "構造・規模・延床":
          this.product_info["構造_規模_延床"] = value
          break
        case "総ｔｏｎ数":
          this.product_info["総ton数"]= value
          break
        default:
          this.product_info[header] = value
          break
      }
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
