<template>
  <v-data-table
    :headers="headerItems"
    :items="dataTableItems"  
    sort-by="calories"
    class="elevation-1"
    :loading = "isLoading"
    loading-text="Loading... Please wait"
    :show-select="showSelect"
    v-model="selected"
    v-on:item-selected="selectedItem"
    :single-select="true"
    :no-data-text="noDataText"
    :height="height"
    fixed-header
    
  >
    <template v-slot:top>
      <v-toolbar
        flat
        dark
        class="toolbar"
        v-if="!disableAddButton"
      >
        <div class="title">{{toobarTitle}}</div>
        <v-spacer></v-spacer>
         <v-btn 
            class="ma-2 add-button"
            v-show="!disableAddButton"
            v-on:click="addItem"
            :disabled="disableAddButton"
          >
            Add Item
          </v-btn>
      </v-toolbar>
    </template>
    <!-- eslint-disable  -->
    <template  v-slot:item.input="item" >
      <!-- eslint-enable -->
      <v-icon
        small
        class="ml-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        v-on:click="deleteItem(item)"
        class="ml-2"
        small
      >
        mdi-delete
      </v-icon>
    </template>
    <!-- eslint-disable  -->
    <template  v-slot:item.inputDelete="item" >
      <!-- eslint-enable -->
      <v-icon
        small
        class="ml-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
    </template>
    <!-- eslint-disable  -->
    <template  v-slot:item.feature="item" >
      <!-- eslint-enable -->
      <div class="mt-5">
        <custom-combo-box
            
        >
        </custom-combo-box>
      </div>
    </template>
    <!-- eslint-disable  -->
    <template  v-slot:item.actions="item" >
       <!-- eslint-enable -->
       <v-row align-content="center" class="mt-1 mb-1">
          <v-col>
            <v-btn 
              block 
              class="table-action-btn" 
              rounded
              v-on:click="emitEvent(item,1)"
              dark>
              {{$t('Download')}}
            </v-btn>
          </v-col> 
          <v-col>
            <v-btn 
              block 
              class="table-action-btn2" 
              rounded v-on:click="emitEvent(item,2)" dark>
              {{$t('Detailed')}}
            </v-btn>
          </v-col> 
       </v-row>
    </template>
  </v-data-table>
</template>
<style lang="scss" scoped>
  .add-button{
    background-color: $button-color !important;
    color: $border-color
  }
  .headline{
    margin-bottom: 2rem;
  }
  .table-action-btn{
    background-color: $main-theme !important;
  }
  .table-action-btn2{
    background-color: $button-color !important;
    color: $call-to-action !important;
  }
  .table-delete-btn{
    background-color: $delete-button-color !important;
  }
  .toolbar{
    background-color: $main-theme !important;
  }
</style>
<script>
export default {
  props:{

    //Loading table
    isLoading:{
      type: Boolean,
      default: false,
    },
    // Data table data
    dataTableItems: {
      type: Array,
      default:function () {
            return [
                
            ]
      },
    },
    noDataText:{
      type:String,
      default: "There is no data in the table"
    },
    height:{
      type:String,
      default: ""
    },
    toobarTitle:{
      type:String,
      default: ""
    },
    selectedItems:{
      type: Array,
      default:function () {
            return [
                
            ]
      },
    },
    // Editable or not?
    editable:{
        type: Boolean,
        default: false,
    }, 
    // Editable or not?
    showSelect:{
        type: Boolean,
        default: false,
    }, 
    // Editable or not?
    isBanner:{
        type: Boolean,
        default: false,
    },    
    defaultPageSize:{
        type: Number,
        default: 5,
    },
    disableAddButton:{
        type: Boolean,
        default: true,
    },
    // show all line if true
    isShowAll:{
        type: Boolean,
        default: false,
    },    
    // Headers
    headerItems: {
      type: Array,
      default:function () {
            return [
                {
                text: 'Dessert (100g serving)',
                align: 'start',
                sortable: false,
                value: 'name',
                },
                { text: 'Calories', value: 'calories' },
                { text: 'Fat (g)', value: 'fat' },
                { text: 'Carbs (g)', value: 'carbs' },
                { text: 'Protein (g)', value: 'protein' },
               
            ]
      },
    },
  },
  watch:{
    dialog (val) {
        val || this.close()
        },
        dialogDelete (val) {
            val || this.closeDelete()
        },
    },

    mounted () {
        // Add action functions
        if(this.editable){
            this.headerItems.push({ text: 'Actions', value: 'actions', sortable: false });  
        }
    },
  computed:{
    formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
    mini() {
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return true
          case 'sm': return true
          case 'md': return false
          case 'lg': return false
          case 'xl': return false
      };
      },
    },
    
    data: () => ({
      snack: false,
      snackColor: '',
      snackText: '',
      selected:[],
      max25chars: v => v.length <= 25 || 'Input too long!',
      dialog: false,
      dialogDelete: false,
      dataItems: [],
      editedIndex: -1,
      editedItem: {
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
    }),
    
    methods: {
        defaultSelected(){
          this.selected.push(this.dataTableItems[0])
        },
        emitEvent(item , idEvent){
          var me = this;
          switch(idEvent)
          {
            case 1:
              me.$emit('download', item.item ,idEvent)
              break
            case 2:
              me.$emit('openLink', item.item ,idEvent)
              break
            case 3:
              me.$emit('openlink', item.item , idEvent)
              break
            default:
              break
          }
        },
        clearItems(){
          console.log('clear table')
        },
        // Edit all items in a row
        editItem (item) {
          this.$emit("edit",item);
        },
        // Delete a row
        deleteItem (item) {
          this.$emit("delete",item);
        },
        // Add Item
        addItem(item){
          this.$emit("add",item);
        },
        // Delete items inrows
        // reset  item if cancel
        closeItemDialog () {
            this.dialog = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },
        selectedItem(item){
          this.$emit("selected",  item)
        },
        // Save item in table
        save () {
            if (this.editedIndex > -1) {
                Object.assign(this.dataTableItems[this.editedIndex], this.editedItem)
            } else {
                this.dataTableItems.push(this.editedItem)
            }
            this.$emit('saveItem', this.editedItem)
            this.close()
        },
        cancel () {
            this.snack = true
            this.snackColor = 'error'
            this.snackText = 'Canceled'
        },
        open () {
            this.snack = true
            this.snackColor = 'info'
            this.snackText = 'Dialog opened'
        },
        close() {
           this.dialog = false
        },
    },  
  }
</script>
