<script setup>
import ConfiguratorContent from "./Configurator-Content.vue";
import { getAPI } from "../../axios";
</script>

<template>
    <div
        class="modal"
        :id="`step-${category.id}`"
        data-bs-backdrop="static"
        data-bs-keyboard="false"
        tabindex="-1"
        aria-labelledby="configuratorModalLabel"
        aria-hidden="true"
    >
        <div
            class="modal-dialog modal-xl modal-dialog-centered modal-fullscreen-lg-down"
        >
            <div class="modal-content modal-dark">
                <div class="modal-header">
                    <h1 class="modal-title fs-5">Choose: {{ category.name }}</h1>
                    <button
                        class="btn-close btn-close-white"
                        type="button"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                    ></button>
                </div>

                <div class="modal-body">
                    <div class="container-fluid text-center h-100">
                        <div
                            class="configurator-body row d-block d-lg-flex text-center"
                        >
                            <div
                                class="img-container col-lg-4 d-flex justify-content-center align-items-center"
                            >
                                <img
                                    src=""
                                    alt=""
                                    class="img-fluid img-guitar-preview"
                                />
                            </div>

                            <div class="col-lg-8 input-col">
                                <div
                                    class="options-container overflow-auto my-2"
                                >
                                    <div class="form-check">
                                        <template v-for="item in items" :key="item.id">
                                            <label
                                                v-if="
                                                    item.category == category.id
                                                "
                                                class=""
                                            >
                                                <div
                                                    v-if="
                                                        category.slug ==
                                                        'miscellaneous'
                                                    "
                                                >
                                                    <input
                                                        class="config-input"
                                                        type="checkbox"
                                                        :name="`check-${item.slug}`"
                                                        :value="`${item.id}`"
                                                        :data-price="`${item.price}`"
                                                    />
                                                    <span class="config-btn">
                                                        <i
                                                            class="bi bi-check-square"
                                                        ></i>
                                                        <div class="config-content">
                                                            <img
                                                                :src="`${item.image_url}`"
                                                                alt=""
                                                                class="config-img"
                                                            />
                                                            <h3
                                                                class="config-title"
                                                            >
                                                                {{ item.name }}
                                                            </h3>
                                                            <p
                                                                class="text-color-success fs-6 config-price-text"
                                                            >
                                                                +{{ item.price }}€
                                                            </p>
                                                        </div>
                                                    </span>
                                                </div>
                                                <div v-else>
                                                    <input
                                                        class="config-input"
                                                        type="radio"
                                                        :name="`radio-${category.id}`"
                                                        :value="`${item.id}`"
                                                        :data-price="`${item.price}`"
                                                    />
                                                    <span class="config-btn">
                                                        <i
                                                            class="bi bi-check-circle"
                                                        ></i>
                                                        <div class="config-content">
                                                            <img
                                                                :src="`${item.image_url}`"
                                                                alt=""
                                                                class="config-img"
                                                            />
                                                            <h3
                                                                class="config-title"
                                                            >
                                                                {{ item.name }}
                                                            </h3>
                                                            <p
                                                                class="text-color-success fs-6 config-price-text"
                                                            >
                                                                +{{ item.price }}€
                                                            </p>
                                                        </div>
                                                    </span>
                                                </div>
                                            </label>
                                        </template>
                                    </div>
                                </div>
                                <button
                                    
                                    class="btn btn-info my-2"
                                    type="submit"
                                    name="save-and-quit"
                                >
                                    Save configuration and quit
                                </button>
                                <button
                                    v-if="category.id == max_steps"
                                    class="btn btn-success my-2"
                                    type="submit"
                                    name="add-to-cart"
                                >
                                    Complete and add to cart
                                </button>
                                <button
                                    v-else
                                    class="btn btn-success my-2"
                                    type="submit"
                                    name="add-to-cart"
                                    disabled
                                >
                                    Complete and add to cart
                                </button>
                                <p
                                    class="text-color-success my-2"
                                    :id="`priceText-${category.id}`"
                                >
                                    Total: €<span
                                        class="currentPrice"
                                        :id="`currentPrice-${category.id}`"
                                        >0.00</span
                                    >
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="modal-footer d-flex justify-content-center">
                    <button
                        class="btn btn-outline-info"
                        v-if="category.id == 1"
                        disabled
                    >
                        <i class="bi bi-caret-left-fill"></i>
                    </button>
                    <button
                        v-else
                        :id="`previousStep-${category.id}`"
                        type="button"
                        class="btn btn-outline-info previousStepButton"
                        :data-bs-target="`#step-${category.id - 1}`"
                        data-bs-toggle="modal"
                    >
                        <i class="bi bi-caret-left-fill"></i>
                    </button>

                    <div class="progress w-25" style="height: 2rem">
                        <div
                            class="progress-bar text-center"
                            role="progressbar"
                            aria-label="Configurator progress"
                            aria-valuemin="0"
                            :aria-valuemax="max_steps"
                            :aria-valuenow="category.id"
                            :style="`width: calc(100% / ${max_steps} * ${category.id})`"
                        >
                            {{ category.id }} / {{ max_steps }}
                        </div>
                    </div>

                    <button
                        class="btn btn-outline-info"
                        v-if="category.id == max_steps"
                        disabled
                    >
                        <i class="bi bi-caret-right-fill"></i>
                    </button>
                    <button
                        v-else
                        :id="`nextStep-${category.id}`"
                        type="button"
                        class="btn btn-outline-info nextStepButton"
                        :data-bs-target="`#step-${category.id + 1}`"
                        data-bs-toggle="modal"
                    >
                        <i class="bi bi-caret-right-fill"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ConfiguratorModal",
    components: {
        ConfiguratorContent,
    },
    props: ["category", "items", "step", "max_steps"],
};
</script>
<style scoped></style>
