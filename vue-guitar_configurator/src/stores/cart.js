import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'

export const useCartStore = defineStore('cart', {
    //state
    state: () => ({
        cart: { 
            configurations: []
        },
    }),

    //getters

    actions: {
        init() {
            if(localStorage.getItem('cart')){
                this.cart = JSON.parse(localStorage.getItem('cart'))
            }else{
                localStorage.setItem('cart', JSON.stringify(this.cart))
            }
        },
        //add items one by one or as one full configuration?
        addToCart(configuration) {
            const exists = this.cart.configurations.filter(i => i.id === configuration.id)

            if (exists.length) {
                exists[0].quantity = parseInt(exists[0].quantity) + parseInt(configuration.quantity)
            } else {
                this.cart.configurations.push(configuration)
            }

            localStorage.setItem('cart', JSON.stringify(this.cart))
        }
    },
})
