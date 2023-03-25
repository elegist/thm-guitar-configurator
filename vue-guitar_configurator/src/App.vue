<script setup>
//import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import { useUserStore } from "./stores/user"
import axios from 'axios'

const userStore = useUserStore()
userStore.init()
const token = userStore.token

if (token) {
  axios.defaults.headers.common['Authorization'] = "Token " + token
} else {
  axios.defaults.headers.common['Authorization'] = ""
}
</script>

<template>
  
  <Navbar />
  <RouterView />
  <Footer />
</template>

