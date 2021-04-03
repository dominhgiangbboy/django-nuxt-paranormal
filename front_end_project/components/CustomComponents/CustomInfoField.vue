<template>
  <div class="custom-field">
    <div class="header-title" :style="colorHeader== '' ?'':'background-color:'+ colorHeader + '!important'">
      {{labelHeader}}
    </div>
    <div class="field-body">
      <v-text-field
      v-model="textValue"
      v-bind:value="value"
      v-on:input="input($event)"
      class="field-text"
      :readonly="readOnly"
      :disabled="disabled"
      :background-color="bgColor==''?'':bgColor"
      outlined
      >

      </v-text-field>
    </div>
  </div>
</template>
<style lang="scss" scoped>
  .custom-btn{
    background-color: $main-theme !important;
  }
  .header-title{
    background-color: $main-theme;
    color: $text-color;
    padding: 0.5rem;
    text-align: center;
  }
  .field-text{
    // border: 1px solid $border-color;
    border-radius: 0px !important;
  }
</style>
<script>
export default {
  props:{
    bgColor:{
      type: String,
      default:'',
    },
    readOnly:{
      type: Boolean,
      default: false
    },
    disabled:{
      type: Boolean,
      default: false
    },
    value:{
      type: String,
      default:'',
    },
    colorHeader:{
      type: String,
      default:'',
    },
    drawer: {
      type: Boolean,
      default: false
    },
    labelHeader: {
      type: String,
      default: 'Header'
    },
    textField:{
      default: ''
    },
  },
  watch:{
  
  },
    computed:{
      mini() {
            switch (this.$vuetify.breakpoint.name) {
              case 'xs': return true
              case 'sm': return true
              case 'md': return true
              case 'lg': return false
              case 'xl': return false
          };
      },
      textValue: {
        // get value from this.textField
        get: function () {
          return this.textField
        },
        // set value to props
        set: function (newValue) {
          //  this.textField = newValue
        }
      },
    },
    data: () => ({
      select: '',
    }),
    methods: {
        input(value){
          this.$emit('input',value, this.labelHeader)
        },
        clicked(){
          this.$emit('click')
        },
    },  
  }
</script>
