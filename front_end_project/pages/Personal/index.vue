<template>
  <v-container fluid>
    <!-- <v-row>
      <v-col  :cols="mini?'12':'3'">
          <custom-combo-box
            label="Choose my analyzed data"
          >
          </custom-combo-box>
      </v-col>
      <v-col :cols="mini?'12':'3'">
        <custom-button label="search">

        </custom-button>
      </v-col>
    </v-row> -->
    <v-row>
        <v-col :cols="mini?'12':'6'">
          <custom-table
                :defaultPageSize="10"
                :headerItems="tableHeaders"
                :isLoading="isLoading"
                :dataTableItems="tableItems"
                :singleSelect="true"
                dense
                :showSelect="true"
                v-on:selected="selectItem"
                :isShowAll="false"
                :isBanner="true"
                v-on:edit="editItem"
                v-on:delete="deleteItem"
                :toobarTitle="$t('My dataset list')"
                :disableAddButton="true"
                height="500"
            >
          </custom-table>
        </v-col>
        <v-col :cols="mini?'12':'6'">
          <v-row>
            <div class="text-header">
              {{$t('Preview data')}}
            </div>
          </v-row>
          <v-row>
            <div class="json-field">
              <pre>{{ jsonstr | pretty }}</pre>
            </div>
          </v-row>
          
        </v-col>
    </v-row>
    <!-- <v-row>
      <v-col cols="6">
        <v-text-field
          class="mr-5 mt-5"
          label="Choose published data to compare"
          rounded
          dense
          outlined
        >
        </v-text-field>
        <custom-button 
          class="mr-5  mt-5"
          label="Search"
          >

        </custom-button>
      </v-col>
      
    </v-row>
    <v-row>
      <v-col cols="6">

      </v-col>
      <v-col cols="6">
        <canvas id="my-chart"></canvas>  
      </v-col>
    </v-row> -->
  </v-container>
</template>
<style lang="scss" scoped>
  .text-header{
    margin: 1rem;
    font-size: 1.5rem;
    font-weight: bold;
    color: $main-theme;
  }
  .json-field{
    background-color: #dee2e6;
    width: 100%;
    max-height: 50vh;
    padding: 1rem;
    margin-right: 1rem;
    overflow: auto;
  }
</style>
<script>
import Chart from 'chart.js';
import * as ChartAnnotation from 'chartjs-plugin-annotation';

export default {
  data() {
    return {
      get_data_set_api: "data-analysis-get-user/",
      delete_data_api: "data-analysis-delete/",
      showUpdate:false,
      isLoading:false,
      comboBoxItems: [],
      tableItems: [
      ],
      jsonstr: '',
      tableHeaders: [
        
      ],
      infoField: '',
      userID: 0,
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
    me.comboBoxGet();
    // me.createdChart();
    me.init()
  },
  created () {
    this.tableHeaders = [
      {
        text: this.$t("User analysis"),
        align: 'start',
        sortable: false,
        value: 'name',
        edditable: true,
      },
      {
        text: this.$t("Information"),
        align: 'start',
        sortable: false,
        value: 'information',
        edditable: true,
      },
      {
        text: '',
        align: 'start',
        sortable: false,
        width: 100,
        value: 'input',
      },
    ]
    this.userID = this.getCookie("userID")
  },
  methods: {
    async init (){
      this.getDataSetDetail();
    },
    async getDataSetDetail(){
      var me = this;  
      var dataReq =
      {
        "user_id": me.userID,
      };
      me.postToServer(dataReq,me.get_data_set_api).then((res)=>{  
        me.tableItems = res
      })
    },
   async clickButton () {
    
   },
   deleteItem(item){
     var me = this
     me.swAlert(
       'Delete'
       , 'Are you sure you want to delete this row?'
       , 'question', ()=>{me.deleteAction(item.item.id)})
   },
   deleteAction(id){
    var me = this;  
    var dataReq =
    {
      "id": id,
    };
    me.postToServer(dataReq,me.delete_data_api).then((res)=>{  
      me.swAlert(
       'Delete'
       , 'Delete row successfuly'
       , 'success', ()=>{
         return;
       })
    })
   },
   async editItem(item){
     var me = this
   },
   insertClick(){
   },
   // Get combo box items
   async comboBoxGet(){
     var me = this;
   },
   async clickButton2 () {
      var me = this;

     // me.$axios.$get('http://127.0.0.1:8000/api/user/users/', loginData)
   
    },
    changeRoute(){
      var me =this;
      me.$nuxt.$router.push(me.localePath('/master'))
    },
    clear() {
      this.$refs.form.reset();
    },
    //
    selectItem(item){
      this.jsonstr = item.item.json
    },
    // Created chart function
    // createdChart(){
    //   new Chart(document.getElementById('my-chart'), {
    //     plugins: [ChartAnnotation],
    //     options: {
    //         annotation: {
    //           annotations: [
    //             {
    //               drawTime: "afterDatasetsDraw",
    //               id: "anno-1",
    //               type: "line",
    //               mode: "horizontal",
    //               scaleID: "y-axis-0",
    //               value: 1000,
    //               borderColor: "#FFA259",
    //               borderWidth: 2,
    //               label: {
    //                 backgroundColor: "#FFA259",
    //                 content: "Line 1",
    //                 enabled: true
    //               }
    //             },
    //             {
    //               drawTime: "afterDatasetsDraw",
    //               id: "anno-2",
    //               type: "line",
    //               mode: "horizontal",
    //               scaleID: "y-axis-0",
    //               value: 1200,
    //               borderColor: "#00af91",
    //               borderWidth: 2,
    //               label: {
    //                 backgroundColor: "#00af91",
    //                 content: "Line 2",
    //                 enabled: true
    //               }
    //             },
    //           ]
    //         },
    //         scales: {
    //             xAxes: [{
                    
    //                 stacked: true,
    //                 gridLines: {
    //                     display:false
    //                 }
    //             }],
    //             yAxes: [{
    //                 ticks: {
    //                         // Include a dollar sign in the ticks
    //                         callback: function(value, index, values) {
    //                             return '¥' + value  ;
    //                         }
    //                 },
    //                 stacked: true,
                    
    //             }]
    //         }
    //     },
    //     type: 'bar',
    //     data: {
    //       labels: ['1月', '2月', '3月', '4月', '5月','6月', '7月', '8月', '9月', '10月', '11月', '12月'],
    //       datasets: [
    //         {
    //           label: '1',
    //           backgroundColor: '#2C73D2',
    //           options: {
    //               scales: {
    //                   xAxes: [{
    //                       stacked: true
    //                   }],
    //                   yAxes: [{
    //                       stacked: true
    //                   }]
    //               }
    //           },
    //           data: [
    //             { x: 1, y: 300 },
    //             { x: 1, y: 700 },
    //             { x: 1, y: 450 },
    //             { x: 3, y: 750 },
    //             { x: 4, y: 450 },
    //             { x: 1, y: 300 },
    //             { x: 1, y: 700 },
    //             { x: 1, y: 450 },
    //             { x: 3, y: 750 },
    //             { x: 4, y: 450 },
    //             { x: 3, y: 750 },
    //             { x: 4, y: 450 },
    //             ]
    //         },
    //         {
    //           label: '2',
    //           backgroundColor: '#e45826',
    //           options: {
    //               scales: {
    //                   xAxes: [{
    //                       stacked: true
    //                   }],
    //                   yAxes: [{
    //                       stacked: true
    //                   }]
    //               }
    //           },
    //           data: [
    //             { x: 1, y: 300 },
    //             { x: 1, y: 700 },
    //             { x: 1, y: 450 },
    //             { x: 3, y: 750 },
    //             { x: 4, y: 450 },
    //             { x: 1, y: 300 },
    //             { x: 1, y: 700 },
    //             { x: 1, y: 450 },
    //             { x: 3, y: 750 },
    //             { x: 4, y: 450 },
    //             { x: 3, y: 750 },
    //             { x: 4, y: 450 },
    //           ]
    //         }
    //       ]
    //     }
    //   });
      
    // },
  }
};
</script>
