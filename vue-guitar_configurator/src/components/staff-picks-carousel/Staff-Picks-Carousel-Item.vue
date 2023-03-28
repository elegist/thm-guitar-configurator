<script setup>
import axios from 'axios';
import { useCartStore } from '../../stores/cart';
</script>

<template>
    <div class="container w-50 py-5 text-center">
        <div class="row">
            <div class="col">
                <h3>{{ pick.name }}</h3>

                <img class="img-fluid" :src="image" alt="" />

                <p class="text-color-success pt-3">{{ pick.total_price }}€</p>
                <div class="d-grid gap-2 col-sm mx-auto">
                    <button
                        @click="addToCart"
                        class="btn btn-success shadow-sm mt-2 mt-md-0"
                        >Add to cart</button
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
                        {{ item }}
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
            cartStore: useCartStore(),
        };
    },
    created() {
        // this.pick.configuration_items.forEach((configurationItem) => {
        //     this.configurationItems.push(
        //         this.items.filter((item) => {
        //             return item.id == configurationItem;
        //         })
        //     );
        // });

        axios
            .get(`api/v1/configuration-items/${this.pick.id}`)
            .then(response => {
                console.log(response.data);
                response.data.items.forEach((data) => {
                    this.configurationItems.push(data)
                })
                this.image = response.data.images[0]
            })

        //this.image = this.configurationItems[0][0].get_image
    },
    methods: {
        addToCart() {
            const configuration = this.pick

            this.cartStore.addToCart(configuration)
        }
    }
};
</script>
