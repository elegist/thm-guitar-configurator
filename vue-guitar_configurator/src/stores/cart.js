import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'

export const useCartStore = defineStore('cart', {
    //state
    state: () => ({
        cart: { 
            cartItems: []
        },
    }),

    //getters

    actions: {
        
    }
})
