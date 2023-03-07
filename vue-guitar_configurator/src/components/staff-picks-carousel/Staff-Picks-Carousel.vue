<script setup>

</script>

<template>
<div class="container mt-5">
    <div
        class="carousel slide text-center"
        id="carouselStaffPicks"
        data-bs-ride="carousel"
        data-bs-interval="5000"
        data-bs-touch="true"
    >
        <div class="carousel-indicators">
            <button
                class="active"
                type="button"
                data-bs-target="#carouselStaffPicks"
                data-bs-slide-to="1"
                aria-current="true"
                aria-label="1"
            ></button>
        </div>

        <div class="carousel-inner">
            <div class="carousel-item active">
                
            </div>
            
                <div class="carousel-item {% if pick == staffPicks|first %} active {% endif %}">
                    
                </div>
            
        </div>

        <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselStaffPicks"
            data-bs-slide="prev"
        >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>

        <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselStaffPicks"
            data-bs-slide="next"
        >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</div>

</template>

<style scoped>

</style>
