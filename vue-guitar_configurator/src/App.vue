<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
</script>

<template>
  <div class="wrapper">
    <Navbar />
    <div id="mainContent" class="container bg-custom-light shadow-lg text-center">
      <RouterView />
    </div>
    <Footer />
  </div>
</template>

