import Vue from 'vue'
import VueSweetalert2 from 'vue-sweetalert2';
import CustomTable from '../components/CustomComponents/CustomTable.vue';
import CustomComboBox from '../components/CustomComponents/CustomComboBox.vue';
import CustomDateTime from '../components/CustomComponents/CustomDateTimePicker.vue';
import CustomButton from '../components/CustomComponents/CustomButton.vue';
import CustomInfoField from '../components/CustomComponents/CustomInfoField.vue';
import CountryFlag from 'vue-country-flag'


// If you don't need the styles, do not connect
import 'sweetalert2/dist/sweetalert2.min.css';

Vue.use(VueSweetalert2);
Vue.component('country-flag', CountryFlag)
Vue.component('custom-table', CustomTable)
Vue.component('custom-combo-box', CustomComboBox)
Vue.component('custom-button', CustomButton)
Vue.component('custom-info-field', CustomInfoField)
Vue.component('custom-date-field', CustomDateTime)