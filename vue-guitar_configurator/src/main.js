import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import BootstrapIcon from '@dvuckovic/vue3-bootstrap-icons'; // remove and use "bootstrap-icons/font/bootstrap-icons.css" instead

import "bootstrap-icons/font/bootstrap-icons.css";
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import './assets/styles/configurator-buttons.css'


const app = createApp(App)

app.use(createPinia())
app.component('BootstrapIcon', BootstrapIcon)
app.use(router)
app.mount('#app')
