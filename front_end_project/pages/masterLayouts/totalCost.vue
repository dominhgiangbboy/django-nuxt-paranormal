<template>
  <v-container class="container" fluid>
    <v-row>
        <v-col :cols="mini?12:2" :class="mini?'combobox-header-left mt-2':'combobox-header mt-2'">
            集計結果１内分類
        </v-col>
        <v-col>
            <custom-combo-box style="max-width:300px" label="選択してください">

            </custom-combo-box>
        </v-col>
    </v-row>
    <v-card outlined>
        <v-card-title>
            {{title}}
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col :cols="mini?12:4">
                    <custom-info-field label-header="営業予算金額">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?12:4">
                    <custom-info-field label-header="実行予算金額">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?12:4"> 
                    <custom-info-field label-header="実施金額">

                    </custom-info-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col :cols="mini?12:4">
                    <custom-info-field label-header="営業予算対実行予算差額合計" color-header="#5aa739">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?12:4">
                    <custom-info-field label-header="営業予算対実施金額差額合計" color-header="#5aa739">

                    </custom-info-field>
                </v-col>
                <v-col :cols="mini?12:4">
                    <custom-info-field :label-header="'実行予算対実施金額差額合計'" color-header="#5aa739">

                    </custom-info-field>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
  </v-container>
</template>
<style lang="scss" scoped>
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
      isLoading: false,
      title: "",
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
