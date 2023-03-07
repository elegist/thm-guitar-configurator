<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import HomeView from './views/HomeView.vue';
</script>

<template>
  
  <Navbar />
  <HomeView />
  <Footer />
  <RouterView />
</template>

