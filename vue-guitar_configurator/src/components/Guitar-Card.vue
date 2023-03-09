
<template>
<div class="card guitar-card mx-auto" style="max-width: 18rem">
    <img
        class="m-2 rounded"
        :src="model.get_image"
        alt=""
        srcset=""
    />
    <hr class="my-2" />
    <h4 class="card-title">{{ model.name }}</h4>
    <hr class="my-2" />
    <div class="d-flex justify-content-around">
        <p class="fw-light">Starts at</p>
        <p class="fw-bold fst-italic text-color-success">€ {{ model.price }}</p>
    </div>
    <div class="d-grid gap-2 col-6 mx-auto my-2">
        <button class="btn btn-info btn-lg" type="button" data-bs-toggle="modal" :data-bs-target="`#${model.name}-configuratorModalStep1`">Configure</button>
    </div>
</div>


</template>

<script>
    export default{
        name: "GuitarCard",
        props: ['model']
    }
</script>
<style scoped>

</style>
