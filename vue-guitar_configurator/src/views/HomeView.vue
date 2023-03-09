<script setup>
  import ConfigureYourOwn from '../components/Configure-Your-Own.vue';
  import Hero from '../components/Hero.vue';
  import StaffPicks from '../components/staff-picks-carousel/Staff-Picks.vue';
  import ConfiguratorModal from '../components/configurator/Configurator-Modal.vue'
  import CartOffCanvas from '../components/cart/cart-offcanvas.vue'
  import { getAPI } from '../axios';
</script>

<template>
  <main>
    <!-- Shopping Cart -->
    <CartOffCanvas />
  
    <!-- Configurator Modals -->
    <template v-for="model in APIData" :key="model.id">
      <ConfiguratorModal :model="model" :step="1" :maxStep="6"/>
      <ConfiguratorModal :model="model" :step="2" :maxStep="6"/>
      <ConfiguratorModal :model="model" :step="3" :maxStep="6"/>
      <ConfiguratorModal :model="model" :step="4" :maxStep="6"/>
      <ConfiguratorModal :model="model" :step="5" :maxStep="6"/>
      <ConfiguratorModal :model="model" :step="6" :maxStep="6"/>
    </template>
    <ConfiguratorContent />
    <div class="container bg-custom-light shadow-lg">
      <Hero />
      <div class="container py-3">
        <StaffPicks />
      </div>
      <div class="container py-5">
        <ConfigureYourOwn />
      </div>
    </div>
  </main>
</template>


<script>
    export default {
        name: 'HomeView',
        data(){
            return {
                APIData: []
            }
        },
        components: {
        },
        created (){
            getAPI.get('/api/v1/model/',)
            .then(response => {
                console.log('data fetch from API successful')
                this.APIData = response.data
            })
            .catch(error => {
                console.log(error)
            })    
        }
    }
</script>
