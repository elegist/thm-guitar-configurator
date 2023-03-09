
<template>
<div
    class="offcanvas offcanvas-end bg-custom-dark"
    tabindex="-1"
    id="offcanvasCart"
    aria-labelledby="offcanvasCartLabel"
>
    <div class="offcanvas-header">
        <h1 class="offcanvas-title" id="offcanvasCartLabel">
            Cart
        </h1>
        <button
            type="button"
            class="btn-close btn-close-white"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
        ></button>
    </div>
    <div class="offcanvas-body">
        <p class="fst-italic text-color-info">No items in cart</p>

        <div class="d-grid gap-2 mt-5">
            <button class="btn btn-success btn-lg" disabled>Order</button>
        </div>
    </div>
</div>
</template>
    
<script>

</script>
<style scoped>

</style>
    