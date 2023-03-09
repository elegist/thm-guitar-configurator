<script setup>

</script>

<template>

<label class="">
    <input class="config-input" type="checkbox" name="checkbox" />
    <span class="config-btn">
        <i class="bi bi-check-square"></i>
        
        <div class="config-content">
            <img src="" alt="" class="config-img" />
            <h3 class="config-title">{{ configuratorItem }}</h3>
            <p class="text-color-success fs-6 config-price-text">+{{ configuratorItem.price }}€</p>
        </div>
    </span>
</label>
</template>

<script>
    export default {
        name:'checkButton',
        pops: ['configuratorItem']
    }
</script>

<style scoped>

</style>
    