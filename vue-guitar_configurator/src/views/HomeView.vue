<script setup>
import Hero from "../components/Hero.vue";
import StaffPicksCarousel from "../components/staff-picks-carousel/Staff-Picks-Carousel.vue";
import ConfiguratorModal from "../components/configurator/Configurator-Modal.vue";
import {storeToRefs} from 'pinia'
import { ref } from 'vue'
import { getAPI } from "../axios";
import { useCartStore } from '../stores/cart'

// const modalForm = ref([])
// function submitCart(){
//     modalForm = {

//     }
// }

</script>

<template>
    <form @submit.prevent="submitCart" id="configurationForm">
        <ConfiguratorModal
            @updateFormSelection="updateS($event)"
            v-for="(category, step) in categories"
            :key="category.id"
            :category="category"
            :items="items"
            :max_steps="max_steps"
            :step="step"
        />
    </form>

    <Hero />

    <StaffPicksCarousel :staffPicks="staffPicks" :items="items"/>
</template>

<script>
export default {
    name: "HomeView",
    data() {
        return {
            categories: [],
            items: [],
            max_steps: 0,
            staffPicks: [],
            radio: [],
            checked: []
        };
    },
    created() {
        getAPI
            .get("/api/v1/category/")
            .then((response) => {
                console.log("data fetch from API successful -> Categories");
                this.categories = response.data;
                this.max_steps = this.categories.length
            })
            .catch((error) => {
                console.log(error);
            });
        getAPI
            .get("/api/v1/item/")
            .then((response) => {
                console.log("data fetch from API successful -> Items");
                this.items = response.data;
            })
            .catch((error) => {
                console.log(error)
            });
        getAPI
            .get("/api/v1/staff-picks/")
            .then((response) => {
                console.log("data fetch from API successful -> Staff Picks");
                this.staffPicks = response.data;
            })
            .catch((error) => {
                console.log(error)
            })
    },
    methods: {
        updateS(checked, radio){
            this.checked=checked;
            this.radio=radio;
        },
        submitCart(){
            const formData = {
                radio: this.radio,
                checked: this.checked
            }
            console.log(this.checked)
        }
    }
};

</script>
