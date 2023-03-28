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
            <template v-if="getCartLength > 0">
                <ol class="list-group">
                    <li
                        v-for="item in items.configurations"
                        class="list-group-item list-group-item-dark"
                    >
                        <img src="" alt="Selected guitar shape" class="w-50" />
                        <div class="d-flex justify-content-between">
                            <div class="fw-bold">{{ item.name }}</div>
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
                                €{{ item.total_price }}
                            </div>
                        </div>
                    </li>
                </ol>
                <div class="d-grid gap-2 mt-5">
                    <span>Total: €</span>
                    <router-link to="/order-summary" class="btn btn-warning btn-lg">
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
export default {
    name: "CartOffCanvas",
    data() {
        return {
            items: [],
            cartStore: useCartStore(),
        };
    },
    mounted() {
        this.items = this.cartStore.cart;
    },
    computed: {
        getCartLength() {
            return this.cartStore.cart.configurations.length;
        },
    },
};
</script>
<style scoped></style>
