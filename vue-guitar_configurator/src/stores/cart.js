import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', {
    //state
    state: () => ({
        cart: { 
            configurations: [],
            stepChoices: [],
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
