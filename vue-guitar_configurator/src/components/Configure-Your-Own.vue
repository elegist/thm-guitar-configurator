<script setup>
import GuitarCard from './Guitar-Card.vue';
import { getAPI } from '../axios';
</script>

<template>
<h1 id="configurator-section" class="text-center">Configure your own!</h1>

<div class="container text-center pt-5">
    <div class="row">
        <div v-for="model in ModelData" :key="model.id" class="col-md-6 col-lg-3 my-2">
          <GuitarCard :model="model"/>  
        </div>
    </div>
</div>
</template>

<script>
    export default {
        name: 'ConfigureYourOwn',
        data(){
            return {
                ModelData: []
            }
        },
        components: {
        },
        created (){
            getAPI.get('/api/v1/model/',)
            .then(response => {
                console.log('data fetch from API successful')
                this.ModelData = response.data
            })
            .catch(error => {
                console.log(error)
            })    
        }
    }
</script>

<style scoped>

</style>
