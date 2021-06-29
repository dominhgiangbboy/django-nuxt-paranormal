<template>
  <v-container class="container" fluid>
    <!-- add Plant dialog -->
    <v-dialog v-model="addDialog" max-width="900px">
      <v-card class="pa-2">
        <v-card-title class="headline mb-5">
          <span>{{ $t("Choose data to upload") }} </span>
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="2" class="mt-1">
              <div>
                Insert your dataset's name
              </div>
            </v-col>
            <v-col>
              <v-text-field
                v-model="tempAddItems['name']"
                type="String"
                outlined
                dense
              >
              </v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="2" class="mt-1">
              <div>
                Data's link in server
              </div>
            </v-col>
            <v-col>
              <v-text-field
                v-model="tempAddItems['link']"
                type="String"
                outlined
                dense
              >
              </v-text-field>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="2" class="mt-1">
              <div>
                Description
              </div>
            </v-col>
            <v-col>
              <v-textarea
                v-model="tempAddItems['description']"
                type="String"
                outlined
                dense
                auto-grow
              >
              </v-textarea>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2" class="mt-1">
              <div>
                Choose category
              </div>
            </v-col>
            <v-col :cols="mini ? '6' : '6'">
              <custom-combo-box
                label="Choose category"
                :comboBoxItems="categoryList"
                :itemValue="currentCategoryID"
                v-on:change="chooseCategory"
              >
              </custom-combo-box>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2" class="mt-1">
              <div>
                Choose type
              </div>
            </v-col>
            <v-col :cols="mini ? '6' : '6'">
              <custom-combo-box
                label="Choose type"
                :itemValue="currentTypeID"
                :comboBoxItems="comboItemType"
                v-on:change="chooseType"
              >
              </custom-combo-box>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <label
                >File
                <input
                  type="file"
                  id="file"
                  ref="file"
                  multiple="multiple"
                  v-on:change="handleFileUploads"
                />
              </label>
              <br />
              <progress max="100" :value.prop="uploadPercentage"></progress>
            </v-col>
            <v-col v-show="currentTypeID == 1">
              <v-row>
                <v-col>
                  <div class="title-link">
                    <span>
                      {{ $t("Insert published links") }}
                    </span>
                  </div>
                </v-col>
              </v-row>
              <v-row
                style="height:60px"
                v-for="(el, index) in links"
                :key="index"
              >
                <v-col
                  ><v-text-field
                    v-model="links[index]"
                    dense
                    outlined
                    :placeholder="$t('Please insert published link')"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-icon
                  class="ml-2"
                  style="cursor:pointer"
                  v-on:click="addLink"
                  size="40"
                >
                  mdi-plus-box
                </v-icon>
              </v-row>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="darken-1" text @click="addDialog = false">
            Cancel
          </v-btn>
          <custom-button v-on:click="submitFile" label="Upload dataset">
          </custom-button>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
      <v-col :cols="mini ? '6' : '3'">
        <custom-combo-box
          :label="$t('Choose category')"
          :comboBoxItems="categoryList"
          :itemValue="currentCategoryID"
          v-on:change="chooseCategory"
        >
        </custom-combo-box>
      </v-col>
      <v-col :cols="mini ? '6' : '3'">
        <custom-combo-box
          :label="$t('Choose type')"
          :comboBoxItems="comboItemType"
          :itemValue="currentTypeID"
          v-on:change="chooseType"
        >
        </custom-combo-box>
      </v-col>
      <custom-button
        class="mt-3"
        v-on:click="getDataSetItems"
        :label="$t('Search')"
      >
      </custom-button>
      <custom-button class="ma-3" v-on:click="openAddDialog" :label="$t('Add')">
      </custom-button>
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
          :isBanner="true"
          v-on:download="downloadFileAction"
          v-on:openLink="openLink"
          v-on:add="createNewDataset"
          :toobarTitle="$t('Data set list')"
          :disableAddButton="true"
          height="500"
        >
        </custom-table>
      </v-col>
    </v-row>
  </v-container>
</template>
<style lang="scss" scoped>
.mb-20 {
  margin-bottom: 4rem;
}
.tab-item {
  padding: 1rem;
}
.combobox-header {
  text-align: right;
  font-weight: bold;
}
.combobox-header-left {
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
    }
  },
  mounted() {
    // get default value
    this.init();
  },
  created() {
    this.userID = this.getCookie("userID");
    let tempIsAdmin = this.getCookie("isAdmin");
    if (tempIsAdmin == "true") {
      this.isAdmin = true;
    } else {
      this.isAdmin = false;
    }
    this.tableHeaders = [
      {
        text: this.$t("Dataset's name"),
        align: "start",
        sortable: false,
        value: "name",
        edditable: true
      },
      {
        text: this.$t("Information"),
        align: "start",
        sortable: false,
        value: "description",
        edditable: true
      },
      {
        text: "",
        align: "start",
        sortable: false,
        width: 200,
        value: "actions"
      }
    ];
  },
  data() {
    return {
      // Plant data
      tableHeaders: [],
      userID: "",
      tableItems: [],
      links: [""],
      addDialog: false,
      isAdmin: false,
      currentPlantID: 0,
      isLoadingPlant: false,
      tempAddItems: {},
      comboItemType: [
        {
          name: "Published data",
          id: 1
        },
        {
          name: "Crawled data from the internet",
          id: 2
        }
      ],
      categoryList: [],
      file: [],
      uploadPercentage: 0,
      currentCategoryID: 0,
      currentTypeID: 0,
      isLoadingProcess: false,
      // SUb process
      tableItemsSubProcess: [],
      //
      action: 0,
      currentItem: 0,
      tab: null,
      isLoading: false,
      dialog: false,
      search: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      tempHeaderItems: {},
      status: false,
      //API link
      get_category_api: "index/category-list-get/",
      get_data_set_api: "data-set-get/"
    };
  },
  methods: {
    async init() {
      this.refreshToken();
      this.getCategory();
      this.getDataSetItems();
      this.currentURL = process.env.BASE_URL;
    },
    openAddDialog() {
      this.addDialog = true;
    },
    addLink(index) {
      this.links.push("");
    },
    async getDataSetItems() {
      var me = this;
      var dataReq = {
        category_id: me.currentCategoryID,
        type_id: me.currentTypeID
      };
      me.postToServer(dataReq, me.get_data_set_api).then(res => {
        me.tableItems = res;
      });
    },
    async uploadData() {
      this.handleFileUpload();
    },
    /*
    Handles a change on the file upload
    */
    handleFileUploads() {
      this.file = this.$refs.file.files;
    },
    submitFile() {
      /*
        Initialize the form data
      */
      var me = this;
      let formData = new FormData();

      /*
        Add the form data we need to submit
      */
      var dummyPost = {
        user: "Giang"
      };
      for (var i = 0; i < me.file.length; i++) {
        let file = me.file[i];
        formData.append("files", file);
      }
      formData.append("name", me.tempAddItems["name"]);
      formData.append("link", me.tempAddItems["link"]);
      formData.append("category", me.currentCategoryID);
      formData.append("user_id", me.userID);
      formData.append("type", me.currentTypeID);
      formData.append("description", me.tempAddItems["description"]);
      /*
        Make the request to the POST /single-file URL
      */

      me.$axios
        .post(me.currentURL + "index/upload-file/", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          },
          onUploadProgress: function(progressEvent) {
            me.uploadPercentage = parseInt(
              Math.round((progressEvent.loaded / progressEvent.total) * 100)
            );
          }.bind(me)
        })
        .then(function() {
          me.swAlert("Success", "Successfully Uploaded", "success", () => {
            me.getDataSetItems();
          });
          me.addDialog = false;
        })
        .catch(function(e) {
          me.swAlert("Failed", e, "error", () => {
            me.getDataSetItems();
          });
          me.addDialog = false;
        });
    },
    // plant actions
    async getCategory() {
      var me = this;
      var dataReq;
      me.postToServer(dataReq, me.get_category_api).then(res => {
        me.categoryList = res;
      });
    },
    selectItemsPlant(item) {
      var me = this;
      if (item.value) {
        var plantID = item.item.id;
        me.currentPlantID = item.item.id;
        me.getPlantProcessItems();
      } else if (!item.value) {
        if (item.item.id == me.currentPlantID) {
          me.currentPlantID = 0;
          me.process_items = [];
        }
      }
    },
    // Process actions
    async getCategoryList() {
      var me = this;
      var dataReq;
      me.postToServer(dataReq, me.get_plant_process_api).then(res => {
        me.tableItemsProcess = res;
      });
    },
    openLink() {},
    downloadFileAction(item) {
      var me = this;
      var dataReq = item;
      me.downloadFile(dataReq, item.name);
    },
    openLink(item) {
      var me = this;

      me.$nuxt.$router.push({
        path: me.localePath("/DetailedPage"),
        query: { dataSetID: item.id }
      });
    },
    createNewDataset() {
      this.addDialog = true;
    },
    chooseCategory(id) {
      this.currentCategoryID = id;
    },
    chooseType(id) {
      this.currentTypeID = id;
    },
    submit() {
      return "";
    },
    buttonclick1() {},
    clear() {
      this.$refs.form.reset();
    }
  }
};
</script>
