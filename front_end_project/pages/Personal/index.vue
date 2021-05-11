<template>
  <v-container fluid>
    <v-row>
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
    </v-row>
    <v-row>
        <v-col :cols="mini?'12':'6'">
          <custom-table
                :defaultPageSize="10"
                :headerItems="tableHeaders"
                :isLoading="isLoading"
                :dataTableItems="tableItems"
                :singleSelect="true"
                dense
                :isShowAll="false"
                :isBanner="true"
                v-on:edit="editItem"
                toobarTitle="My dataset list"
                :disableAddButton="TRUE"
                height="500"
            >
          </custom-table>
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
          <v-row>
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
          </v-row>
          
          <v-row>
            <canvas id="my-chart"></canvas>  
          </v-row>
        </v-col>
    </v-row>
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
      showUpdate:false,
      comboBoxItems: [],
      tableItems: [
        {

        }
      ],
      jsonstr: '{"id":1,"name":"A green door","price":12.50,"tags":["home","green"]}',
      tableHeaders: [
        {
          text: "My Dataset",
          align: 'start',
          sortable: false,
          value: 'name',
          edditable: true,
        },
        {
          text: "Dataset type",
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
          text: '',
          align: 'start',
          sortable: false,
          width: 100,
          value: 'inputDelete',
        },
      ],
      infoField: '',
    };
  },
  filters: {
    pretty: function(value) {
      return JSON.stringify(JSON.parse(value), null, 2);
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
    me.createdChart();
    
  },
  created () {
    this.$nuxt.$on('insertClick', () => {
      this.insertClick();
    })
  },
  methods: {
   async clickButton () {
    
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
      me.$nuxt.$router.push('/master')
    },
    clear() {
      this.$refs.form.reset();
    },
    // Created chart function
    createdChart(){
      new Chart(document.getElementById('my-chart'), {
        plugins: [ChartAnnotation],
        options: {
            annotation: {
              annotations: [
                {
                  drawTime: "afterDatasetsDraw",
                  id: "anno-1",
                  type: "line",
                  mode: "horizontal",
                  scaleID: "y-axis-0",
                  value: 1000,
                  borderColor: "#FFA259",
                  borderWidth: 2,
                  label: {
                    backgroundColor: "#FFA259",
                    content: "Line 1",
                    enabled: true
                  }
                },
                {
                  drawTime: "afterDatasetsDraw",
                  id: "anno-2",
                  type: "line",
                  mode: "horizontal",
                  scaleID: "y-axis-0",
                  value: 1200,
                  borderColor: "#00af91",
                  borderWidth: 2,
                  label: {
                    backgroundColor: "#00af91",
                    content: "Line 2",
                    enabled: true
                  }
                },
              ]
            },
            scales: {
                xAxes: [{
                    
                    stacked: true,
                    gridLines: {
                        display:false
                    }
                }],
                yAxes: [{
                    ticks: {
                            // Include a dollar sign in the ticks
                            callback: function(value, index, values) {
                                return '¥' + value  ;
                            }
                    },
                    stacked: true,
                    
                }]
            }
        },
        type: 'bar',
        data: {
          labels: ['1月', '2月', '3月', '4月', '5月','6月', '7月', '8月', '9月', '10月', '11月', '12月'],
          datasets: [
            {
              label: '1',
              backgroundColor: '#2C73D2',
              options: {
                  scales: {
                      xAxes: [{
                          stacked: true
                      }],
                      yAxes: [{
                          stacked: true
                      }]
                  }
              },
              data: [
                { x: 1, y: 300 },
                { x: 1, y: 700 },
                { x: 1, y: 450 },
                { x: 3, y: 750 },
                { x: 4, y: 450 },
                { x: 1, y: 300 },
                { x: 1, y: 700 },
                { x: 1, y: 450 },
                { x: 3, y: 750 },
                { x: 4, y: 450 },
                { x: 3, y: 750 },
                { x: 4, y: 450 },
                ]
            },
            {
              label: '2',
              backgroundColor: '#e45826',
              options: {
                  scales: {
                      xAxes: [{
                          stacked: true
                      }],
                      yAxes: [{
                          stacked: true
                      }]
                  }
              },
              data: [
                { x: 1, y: 300 },
                { x: 1, y: 700 },
                { x: 1, y: 450 },
                { x: 3, y: 750 },
                { x: 4, y: 450 },
                { x: 1, y: 300 },
                { x: 1, y: 700 },
                { x: 1, y: 450 },
                { x: 3, y: 750 },
                { x: 4, y: 450 },
                { x: 3, y: 750 },
                { x: 4, y: 450 },
              ]
            }
          ]
        }
      });
      
    },
  }
};
</script>
