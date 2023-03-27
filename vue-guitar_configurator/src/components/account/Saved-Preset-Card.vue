<template>
    <div>
        <div class="card guitar-card mx-auto">
            <img class="card-img-top" src="" alt="" />
            <div class="card-body">
                <h3>{{ configuration.name }}</h3>
                <div class="accordion" :id="`accordion-${id}`">
                    <div class="accordion-item">
                        <h2 class="accordion-header">
                            <button
                                class="accordion-button collapsed"
                                type="button"
                                data-bs-toggle="collapse"
                                :data-bs-target="`#content-${id}`"
                                aria-expanded="true"
                                :aria-controls="`#content-${id}`"
                            >
                                Items
                            </button>
                        </h2>
                        <div
                            class="accordion-collapse collapse"
                            :id="`content-${id}`"
                            :data-bs-parent="`#accordion-${id}`"
                        >
                            <div class="accordion-body">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th scope="col">Category</th>
                                            <th scope="col">Item</th>
                                            <th scope="col">Price</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="item in configurationItems">
                                            <td>{{ item[0].category }}</td>
                                            <td>{{ item[0].name }}</td>
                                            <td>€{{ item[0].price }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="d-grid gap-2 col-6 mx-auto my-2">
                    <button class="btn btn-info btn-lg" type="button">
                        Edit
                    </button>
                </div>
            </div>

            <p>Total: €{{ configuration.total_price }}</p>
            <div class="card-footer">
                <small class="text-muted"
                    >Last edited: {{ configuration.date_updated }}</small
                >
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "SavedPresetCard",
    props: ["configuration", "id", "items"],
    data() {
        return {
            configurationItems: [],
        }
    },
    created() {
        this.configuration.configuration_items.forEach((configurationItem) => {
            this.configurationItems.push(
                this.items.filter((item) => {
                    return item.id == configurationItem;
                })
            )
        })
    },
}
</script>

<style scoped></style>
