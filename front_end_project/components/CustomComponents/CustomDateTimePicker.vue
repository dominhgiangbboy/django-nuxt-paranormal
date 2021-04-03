<template>
  <v-menu
      ref="menu1"
      v-model="menu1"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="auto"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          v-model="dateFormatted"
          :label="label"
          persistent-hint
          append-icon="mdi-calendar"
          v-bind="attrs"
          @blur="date = parseDate(dateFormatted)"
          outlined
          dense
          v-on="on"
        ></v-text-field>
      </template>
      <v-date-picker
        v-model="date"
        no-title
        @input="menu1 = false"
      ></v-date-picker>
    </v-menu>
</template>
<style lang="scss" scoped>

</style>
<script>
export default {
    props:{  
      drawer: {
        type: Boolean,
        default: false
      },
      label: {
        type: String,
        default: ''
      },
    },
    watch:{
      date (val) {
        this.dateFormatted = this.formatDate(this.date)
      },
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
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },
     
    data: vm => ({
      date: new Date().toISOString().substr(0, 10),
      dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
      menu1: false,
    }),
    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${month}/${day}/${year}`
      },
      parseDate (date) {
        if (!date) return null

        const [month, day, year] = date.split('/')
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
      },
    },  
  }
</script>
