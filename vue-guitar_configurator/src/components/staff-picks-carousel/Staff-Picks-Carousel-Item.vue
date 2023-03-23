<script setup></script>

<template>
    <div class="container w-50 py-5 text-center">
        <div class="row">
            <div class="col">
                <h3>{{ pick.name }}</h3>

                <img class="img-fluid" :src="image" alt="" />

                <p class="text-color-success pt-3">{{ pick.total_price }}€</p>
                <div class="d-grid gap-2 col-sm mx-auto">
                    <a
                        href="#add-to-cart"
                        class="btn btn-success shadow-sm mt-2 mt-md-0"
                        >Add to cart</a
                    >
                </div>
            </div>
            <div class="col d-none d-lg-block my-auto">
                <ul class="list-group">
                    <li
                        v-for="item in configurationItems"
                        :key="item.id"
                        class="list-group-item list-group-item-dark"
                    >
                        {{ item[0].name }}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "StaffPicksCarouselItem",
    components: {},
    props: ["pick", "items"],
    data() {
        return {
            configurationItems: [],
            image: '',
        };
    },
    created() {
        this.pick.configuration_items.forEach((configurationItem) => {
            this.configurationItems.push(
                this.items.filter((item) => {
                    return item.id == configurationItem;
                })
            );
        });

        this.image = this.configurationItems[0][0].get_image
    },
};
</script>
