<template>
  <v-container fluid>
    <v-row>
      <v-col  :cols="mini?'6':'3'">
        <custom-combo-box
         
        >
        </custom-combo-box>
      </v-col>
       <v-col  :cols="mini?'6':'3'">
        <custom-combo-box
         
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
          label="Search"
        >
        </custom-button>
      </v-col>
      <v-col :cols="mini?'12':'6'"><canvas id="my-chart"></canvas></v-col>
      <v-col :cols="mini?'12':'6'"><canvas id="my-chart-pie"></canvas></v-col>
    </v-row>

  </v-container>
</template>
<style lang="scss" scoped>
  
</style>
<script>
import Chart from 'chart.js';
import * as ChartAnnotation from 'chartjs-plugin-annotation';

export default {
  data() {
    return {
      showUpdate:false,
      comboBoxItems: [],
      infoField: '',
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
      new Chart(document.getElementById('my-chart-pie'), {
        plugins: [ChartAnnotation],
        options: {
            
        },
        type: 'pie',
        data: {
            labels: [
              'Red',
              'Blue',
              'Yellow'
            ],
            datasets: [{
              label: 'My First Dataset',
              data: [300, 50, 100],
              backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
              ],
              hoverOffset: 4
          }],
        }
      });
    },
  }
};
</script>
