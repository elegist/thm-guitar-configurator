<script setup>
  import ConfigureYourOwn from '../components/Configure-Your-Own.vue';
  import Hero from '../components/Hero.vue';
  import StaffPicks from '../components/staff-picks-carousel/Staff-Picks.vue';
</script>

<template>
  <main>
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
