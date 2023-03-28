<template>
    <div
        class="offcanvas offcanvas-end bg-custom-dark"
        tabindex="-1"
        id="offcanvasCart"
        aria-labelledby="offcanvasCartLabel"
    >
        <div class="offcanvas-header">
            <h1 class="offcanvas-title" id="offcanvasCartLabel">Cart</h1>
            <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
            ></button>
        </div>
        <div class="offcanvas-body">
            <template v-if="order">
                <ol class="list-group">
                    <li
                        v-for="(item, index) in orderItems"
                        class="list-group-item list-group-item-dark"
                    >
                        <img src="" alt="Selected guitar shape" class="w-50" />
                        <div class="d-flex justify-content-between">
                            <div class="fw-bold">Name</div>
                            <div class="d-flex gap-2">
                                <a href="#"
                                    ><i class="bi bi-dash-circle"></i
                                ></a>
                                <div>{{ item.quantity }}</div>
                                <a href="#"
                                    ><i class="bi bi-plus-circle"></i
                                ></a>
                            </div>
                            <div class="fw-bold fst-italic text-success">
                                € Price 
                            </div>
                        </div>
                    </li>
                </ol>
                <div class="d-grid gap-2 mt-5">
                    <span>Total: €</span>
                    <router-link
                        to="/order-summary"
                        class="btn btn-warning btn-lg"
                    >
                        Proceed to Checkout
                    </router-link>
                </div>
            </template>
            <template v-else>
                <p class="fst-italic text-color-info">No items in cart</p>

                <div class="d-grid gap-2 mt-5">
                    <button class="btn btn-success btn-lg" disabled>
                        Order
                    </button>
                </div>
            </template>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { useCartStore } from "../../stores/cart";
import { useUserStore } from "../../stores/user";
export default {
    name: "CartOffCanvas",
    data() {
        return {
            userStore: useUserStore(),
            order: null,
            orderItems: [],
        };
    },
    mounted() {
        axios
            .get(`api/v1/order/${this.userStore.customerId}`)
            .then((response) => {
                this.order = response.data;
                return response.data.configurations;
            })
            .then((response) => {
                response.forEach((data) => {
                    axios
                        .get(`api/v1/orderItem/${data}`)
                        .then((response) => {
                            this.orderItems.push(response.data);
                        })
                        .catch((error) => console.log(error));
                });
            })
            .catch((error) => console.log(error));
    },
    computed: {
        // getCartLength() {
        //     return this.cartStore.cart.configurations.length;
        // },
    },
};
</script>
<style scoped></style>
