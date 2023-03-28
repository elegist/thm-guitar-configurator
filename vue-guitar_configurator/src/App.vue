<script setup>
//import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import { useUserStore } from "./stores/user"
import axios from 'axios'
import { useCartStore } from './stores/cart';

const userStore = useUserStore()
userStore.init()
const cartStore = useCartStore()
cartStore.init()

const token = userStore.token

if (token) {
  axios.defaults.headers.common['Authorization'] = "Token " + token
} else {
  axios.defaults.headers.common['Authorization'] = ""
}
</script>

<template>
  <div class="wrapper">
    <Navbar :cart="cart"/>
    <div id="mainContent" class="container bg-custom-light shadow-lg text-center">
      <RouterView />
    </div>
    <Footer />
  </div>
</template>

<script>
export default {
  data() {
    return {
      cart: {
        configurations: []
      }
    }
  },
}
</script>

