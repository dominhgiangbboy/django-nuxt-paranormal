<template>
      <v-btn
        class="custom-btn"
        v-on:click="clicked"
        light
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
    font-weight: bold;
    background-color: $call-to-action !important;
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
