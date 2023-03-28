<template>
    <div class="row mt-3">
        <div class="col-lg-5">
            <h2>Order Summary</h2>
            <div class="accordion" id="accordion-test">
                <div
                    v-for="order_item in orderItems"
                    :key="order_item.id"
                    class="accordion-item"
                >
                    <h2
                        class="accordion-header"
                        :id="`heading-${order_item.id}`"
                    >
                        <button
                            class="accordion-button collapsed btn-dark"
                            type="button"
                            data-bs-toggle="collapse"
                            :data-bs-target="`#collapse-${order_item.id}`"
                            aria-expanded="true"
                            :aria-controls="`collapse-${order_item.id}`"
                        >
                            <img
                                src=""
                                alt="Selected guitar shape"
                                class="w-25"
                            />
                            <div class="d-flex gap-4">
                                <div class="fw-bold">{{ order_item.name }}</div>
                                <div>x{{ order_item.quantity }}</div>
                                <div class="fw-bold fst-italic text-success">
                                    €{{ order_item.total_price }}
                                </div>
                            </div>
                        </button>
                    </h2>
                    <div
                        class="accordion-collapse collapse"
                        :id="`collapse-${order_item.id}`"
                        :aria-labelledby="`heading-${order_item.id}`"
                        :data-bs-parent="`#accordion-${order_item.id}`"
                    >
                        <div class="accordion-body bg-dark">
                            <div class="table-responsive">
                                <table class="table table-dark table-striped">
                                    <thead>
                                        <tr>
                                            <th scope="col">Category</th>
                                            <th scope="col">Selected Item</th>
                                            <th scope="col">Price</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <OrderSummaryItems
                                            :configuration_items="
                                                order_item.configuration_items
                                            "
                                            :items="items"
                                        />
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-lg-7">
            <h2>Payment Information</h2>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { useUserStore } from "../stores/user";
import OrderSummaryItems from "../components/cart/order-summary-items.vue";
export default {
    name: "checkout",
    data() {
        return {
            userStore: useUserStore(),
            userOrders: [],
            orderItems: [],
            items: [],
            configurationItems: [],
        };
    },
    created() {
        axios
            .get("api/v1/item/")
            .then((response) => {
                this.items = response.data;
            })
            .catch((error) => console.log(error));

        axios
            .get(`api/v1/customer/${this.userStore.userId}`)
            .then((response) => {
                return response.data.id;
            })
            .then((response) => {
                axios
                    .get(`api/v1/order/${response}`)
                    .then((response) => {
                        this.userOrders = response.data;
                        return response.data[0].configurations;
                    })
                    .then((response) => {
                        response.forEach((configuration) => {
                            axios
                                .get(`api/v1/configuration/${configuration}`)
                                .then((response) => {
                                    this.orderItems = response.data;
                                });
                        });
                    });
            })
            .catch((errors) => console.log(errors));
    },
    components: { OrderSummaryItems },
};
</script>
