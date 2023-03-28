<script setup>
import Hero from "../components/Hero.vue";
import StaffPicksCarousel from "../components/staff-picks-carousel/Staff-Picks-Carousel.vue";
import ConfiguratorModal from "../components/configurator/Configurator-Modal.vue";
import axios from "axios";
import { useUserStore } from "../stores/user";
</script>

<template>
    <form id="configurationForm" method="post" action="">
        <ConfiguratorModal
            v-for="(category, step) in categories"
            :key="category.id"
            :category="category"
            :items="items"
            :max_steps="max_steps"
            :step="step"
            :form="form"
        />
    </form>

    <Hero />

    <StaffPicksCarousel :staffPicks="staffPicks" />
</template>

<script>
export default {
    name: "HomeView",
    data() {
        return {
            userStore: useUserStore(),
            categories: [],
            items: [],
            max_steps: 0,
            staffPicks: [],
            configurations: [], // get user configurations
            form: [],
            test1: "",
            test2: "",
        };
    },
    created() {
        axios
            .get(`/api/v1/customer/${this.userStore.userId}`)
            .then((response) => {
                this.userStore.customerId = response.data.id;
            })
            .catch((error) => {
                console.log(error);
            });

        axios
            .get("/api/v1/category/")
            .then((response) => {
                console.log("data fetch from API successful -> Categories");
                this.categories = response.data;
                this.max_steps = this.categories.length;
            })
            .catch((error) => {
                console.log(error);
            });
        axios
            .get("/api/v1/item/")
            .then((response) => {
                console.log("data fetch from API successful -> Items");
                this.items = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
        axios
            .get("/api/v1/staff-picks/")
            .then((response) => {
                console.log("data fetch from API successful -> Staff Picks");
                this.staffPicks = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
    },
};
</script>
