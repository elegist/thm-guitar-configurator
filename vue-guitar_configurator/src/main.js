import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import BootstrapIcon from '@dvuckovic/vue3-bootstrap-icons'; // remove and use "bootstrap-icons/font/bootstrap-icons.css" instead
import axios from 'axios'

import "bootstrap-icons/font/bootstrap-icons.css";
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import './assets/styles/configurator-buttons.css'

axios.defaults.baseURL = "http://127.0.0.1:8000"

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.component('BootstrapIcon', BootstrapIcon)
app.use(router, axios)
app.mount('#app')
