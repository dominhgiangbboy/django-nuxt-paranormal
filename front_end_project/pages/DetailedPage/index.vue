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
    <v-row>
        <v-col cols="12">
            <div class="title-banner">
                <v-row>
                    <div class="data-name">
                        <span>
                            {{data.name}}
                        </span>
                    </div>
                </v-row>
                <v-row>
                    <div class="data-type">
                        <span>
                            {{data.type}}
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
            <v-tabs-items v-model="tabModel">
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
                                                {{data.description}}
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
                                    v-on:edit="editItem"
                                    toobarTitle="My dataset list"
                                    :disableAddButton="TRUE"
                                    height="400"
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
                        </v-col>
                    </v-row>
                </v-tab-item>
            </v-tabs-items>
        </v-tabs>
    </v-card>
    
  </v-container>
</template>
<style lang="scss" scoped>
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
export default {
  data() {
    return {
      dialog: false,
      tabModel: 0,
      showUpdate:false,
      comboBoxItems: [],
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
  },
  created () {
    this.$nuxt.$on('insertClick', () => {
      this.insertClick();
    })
  },
  methods: {
   
  }
};
</script>
