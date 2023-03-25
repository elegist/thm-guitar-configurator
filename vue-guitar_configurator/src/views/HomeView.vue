<script setup>
import ConfigureYourOwn from "../components/Configure-Your-Own.vue";
import Hero from "../components/Hero.vue";
import StaffPicksCarousel from "../components/staff-picks-carousel/Staff-Picks-Carousel.vue";
import ConfiguratorModal from "../components/configurator/Configurator-Modal.vue";
import CartOffCanvas from "../components/cart/cart-offcanvas.vue";
import { getAPI } from "../axios";
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
        };
    },
    components: {},
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
};

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie("csrftoken");
</script>
