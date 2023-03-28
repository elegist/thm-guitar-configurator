<template>
    <tr v-for="configurationItem in configurationItems">
        <td>{{ configurationItem[0].category }}</td>
        <td>{{ configurationItem[0].name }}</td>
        <td>€ {{ configurationItem[0].price }}</td>
    </tr>
</template>

<script>
export default {
    name: "OrderSummaryItems",
    data() {
        return {
            configurationItems: [],
        }
    },
    props: ["configuration_items", "items"],
    created() {
        this.configuration_items.forEach((configurationItem) => {
            this.configurationItems.push(
                this.items.filter((item) => {
                    return item.id == configurationItem;
                })
            )
        })
    }
}
</script>