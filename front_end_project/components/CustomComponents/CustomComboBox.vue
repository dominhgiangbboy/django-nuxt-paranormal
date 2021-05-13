<template>
      <v-select
          v-model="item"
          :items="itemsData"
          :label="label"
          :value ="itemValue"
          :rules="rules"
          outlined 
          rounded
          dense
          v-on:change="change_data"
          :disabled="disabled"
        ></v-select>
</template>
<style lang="scss" scoped>

</style>
<script>
export default {
  props:{
    rules:{
      type:Array,
       default:function () {
        return [
        ]
      }
    },
    itemValue:{
      type:Number,
      default: 0,
    }, 
    itemText:{
      type:String,
      default: "",
    }, 
    comboBoxItems: {
      type: Array,
      default:function () {
        return [
            {
              name: 'No items', id: 0          
            },
        ]
      },
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
      default: ''
    },
  },
  watch:{
    
  },
  computed:{
      itemsData(){
        var me = this;
        var itemsTemp = [];
        if (me.comboBoxItems.length == 0){ return}
        me.comboBoxItems.forEach(comboBoxItem => {  
            var itemTemp = {text: '', value: 0};
                itemTemp.text = comboBoxItem.name;
                itemTemp.value = comboBoxItem.id;
                itemsTemp.push(itemTemp);
        });
        var item = itemsTemp.filter(function(item){return (item.value == me.itemValue);} );
        this.item =  item[0]
        return itemsTemp;
      },
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
    watch:{

    },
    data: () => ({
      item:[],
      value: null,
    }),
    mounted(){
    
    },
    methods: {
      change_data(){
        this.$emit('change', this.item)
      }
    },  
  }
</script>
