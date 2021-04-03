<template>
  <v-container class="container" fluid>
    <v-card outlined>
      <v-tabs
        v-model="tab"
        background-color="#1d3557"
        class="tab-bar"
        dark
      >
        <v-tab>
          費用
        </v-tab>
        <v-tab>
          費用の項目
        </v-tab>
        <v-tab>
          限界利益
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <!-- Tab 1 -->
        <v-tab-item  
        class="tab-item"
        >
        <v-row class="mt-5 mb-10">
            <v-col :cols="mini?12:2" :class="mini?'combobox-header-left mt-2':'combobox-header mt-2'">
                集計結果２
            </v-col>
            <v-col>
                <custom-combo-box style="max-width:300px" label="選択してください">

                </custom-combo-box>
            </v-col>
          </v-row>
          <v-row> 
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算売上総利益率"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算積上げ加工単価"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="柱加工ton単価営業予算"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算受注加工単価"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算固定費"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算固定費率"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算積上げ加工単価"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算変動費"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業予算変動費率"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業受注（材工）本体単価"
              ></custom-info-field>
            </v-col>
            <v-col :cols="mini?6:3">
              <custom-info-field
                label-header="営業受注（材工）ton当り固定費"
              ></custom-info-field>
            </v-col>
          </v-row>
        </v-tab-item>
        <!-- Tab 2 -->
        <v-tab-item 
        class="tab-item"
        >

        </v-tab-item>
        <!-- Tab 3 -->
        <v-tab-item 
        class="tab-item"
        >
            <v-row>
              <v-col :cols="mini?6:3">
                <custom-info-field
                  label-header="営業予算売上総利益率"
                ></custom-info-field>
              </v-col>
              <v-col :cols="mini?6:3">
                <custom-info-field
                  label-header="営業予算積上げ加工単価"
                ></custom-info-field>
              </v-col>
              <v-col :cols="mini?6:3">
                <custom-info-field
                  label-header="柱加工ton単価営業予算"
                ></custom-info-field>
              </v-col>
            </v-row>
          <v-expansion-panels>
            <!-- 1 sections -->
            <v-expansion-panel
            >
              <v-expansion-panel-header>
                変動費+工作図+原寸
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="上記の取決めの場合の限界利益"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="上記の取決め金額の場合の粗利率"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      colorHeader="#00a8e8"
                      label-header="ton当り限界利益額"
                    ></custom-info-field>
                  </v-col>
                </v-row>          
              </v-expansion-panel-content>
            </v-expansion-panel>
            <!-- 2 sections -->
            <v-expansion-panel
            >
              <v-expansion-panel-header>
                変動費+工作図
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="上記の取決めの場合の限界利益"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="上記の取決め金額の場合の粗利率"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      colorHeader="#00a8e8"
                      label-header="ton当り限界利益額"
                    ></custom-info-field>
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <!-- 3 sections -->
            <v-expansion-panel
            >
              <v-expansion-panel-header>
                変動費
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="限界利益23％の場合の粗利額"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="上記の取決めの場合の限界利益"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      label-header="上記の取決め金額の場合の粗利率"
                    ></custom-info-field>
                  </v-col>
                  <v-col :cols="mini?6:4">
                    <custom-info-field
                      colorHeader="#00a8e8"
                      label-header="ton当り限界利益額"
                    ></custom-info-field>
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </v-container>
</template>
<style lang="scss" scoped>
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
      tab: null,
      isLoading: false,
      title: "資材G所轄　材料補助材料費＆形鋼・鋼板外注一次加工費",
      dialog: false,
      search: "",
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
    };
  },
  methods: {
    init(){
      this.configButton('update',false, true)
      this.configButton('delete', false, true)
    },
    submit() {      
    },
    buttonclick1(){ 
      
    },
    clear() {
      this.$refs.form.reset();
    },
  },
};
</script>
