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
            
        }
    }
})
