<script setup>
import StaffPicksCarouselItem from "./Staff-Picks-Carousel-Item.vue"
</script>

<template>
    <h2>Staff Picks</h2>

    <div class="container mt-5">
        <div
            class="carousel slide text-center"
            id="carouselStaffPicks"
            data-bs-ride="carousel"
            data-bs-interval="5000"
            data-bs-touch="true"
        >
            <div class="carousel-indicators">
                <template v-for="(pick, index) in staffPicks" :key="pick.id">
                    <button
                        v-if="index == 0"
                        class="active"
                        type="button"
                        data-bs-target="#carouselStaffPicks"
                        :data-bs-slide-to="index"
                        aria-current="true"
                        :aria-label="`Slide ${index + 1}`"
                    ></button>
                    <button
                        v-else
                        type="button"
                        data-bs-target="#carouselStaffPicks"
                        :data-bs-slide-to="index"
                        aria-label="1"
                    ></button>
                </template>
            </div>

            <div class="carousel-inner">
                <template v-for="(pick, index) in staffPicks" :key="pick.id">
                    <div v-if="index == 0" class="carousel-item active">
                        <StaffPicksCarouselItem :pick="pick" :items="items"/>
                    </div>
                    <div v-else class="carousel-item">
                        <StaffPicksCarouselItem :pick="pick" :items="items"/>
                    </div>
                </template>
            </div>

            <button
                class="carousel-control-prev"
                type="button"
                data-bs-target="#carouselStaffPicks"
                data-bs-slide="prev"
            >
                <span
                    class="carousel-control-prev-icon"
                    aria-hidden="true"
                ></span>
                <span class="visually-hidden">Previous</span>
            </button>

            <button
                class="carousel-control-next"
                type="button"
                data-bs-target="#carouselStaffPicks"
                data-bs-slide="next"
            >
                <span
                    class="carousel-control-next-icon"
                    aria-hidden="true"
                ></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "StaffPicksCarousel",
    components: {},
    props: ["staffPicks", "items"],
};
</script>

<style scoped></style>
