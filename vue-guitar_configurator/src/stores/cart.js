import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
    //state
    state: () => ({
        cart: { 
            configurations: [],
        },
    }),

    //getters

    actions: {
        init() {
        },
        addToCart(configuration) {
            this.configurations = configuration
        }
    },
    persist: true,
})
