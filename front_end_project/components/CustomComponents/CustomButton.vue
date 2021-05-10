<template>
      <v-btn
        class="custom-btn"
        v-on:click="clicked"
        light
        rounded
        :disabled="disabled"
        :to="link"
        :link="isLink"
        :block="isBlock"
      >
          {{label}}
      </v-btn>
</template>
<style lang="scss" scoped>
  .custom-btn{
    font-weight: bolder !important;
    padding: 1.5rem !important;
    background-color: $call-to-action !important;
    color: $button-color;
  }
</style>
<script>
export default {
  props:{
    isLink:{
      type:Boolean,
      default: false,
    },
    link:{
      type:String,
      default:  '',
    },
    isBlock:{
      type:Boolean,
      default: false,
    },
    drawer: {
      type: Boolean,
      default: false
    },
    disabled: {
      type: Boolean,
      default: false
    },
    label: {
      type: String,
      default: 'Button'
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
    },
    data: () => ({
      select: '',
    }),
    methods: {
        clicked(){
          this.$emit('click')
        },
    },  
  }
</script>
