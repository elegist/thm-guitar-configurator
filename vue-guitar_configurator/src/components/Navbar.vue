<script setup>
import { useUserStore }  from '../stores/user'
import CartOffCanvas from "../components/cart/cart-offcanvas.vue"
import { mapState, mapStores, mapWritableState } from 'pinia'
import axios from 'axios'
import { nextTick } from 'vue';
import {ref} from 'vue'
import { onUpdated, onMounted } from 'vue';
import { storeToRefs } from 'pinia'

const userStore = useUserStore()
const {username, token} = storeToRefs(userStore)


function getUsername(){
    if (token.value) {
    axios.defaults.headers.common['Authorization'] = "Token " + token.value
    } else {
    axios.defaults.headers.common['Authorization'] = ""
    }
    
    axios
        .get("api/v1/users/me",)
        .then(response => {
            
            userStore.$patch({username: response.data.username})
            console.log('logged in as ' + response.data.username)
        })
        .catch(error => {
            console.log(error)
        })  
}

onMounted(() => {
    getUsername()
})





</script>

<template>
    <CartOffCanvas/>
    <nav class="navbar navbar-expand-lg navbar-dark bg-custom-dark shadow">
    <div class="container">
        <router-link to="/" class="navbar-brand">
            <img
                src='images/guitar-configurator-logo.svg'
                width="64"
                height="64"
                alt="logo"
                srcset=""
            />
            Guitar Configurator
        </router-link>
        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <p class="my-auto">
                    <template v-if="userStore.isAuthenticated">
                        Hello, <span class="text-color-info">{{ username }}</span>
                    </template>
                    <template v-else>
                        Hello, <span class="text-color-info">Guest</span>
                    </template>  
                    
                </p>
                <li class="nav-item dropdown mx-3">
                    <a
                        class="nav-link dropdown-toggle"
                        href="#"
                        role="button"
                        data-bs-toggle="dropdown"
                    >
                    <i class="bi bi-person fs-1"></i>
                    </a>
                    <ul class="dropdown-menu">
                        <template v-if="userStore.isAuthenticated">
                            <li>
                                <router-link to="/account" class="dropdown-item">
                                    Account
                                </router-link>
                            </li>
                        </template>
                        <template v-else>
                            <li>
                                <router-link to="/login" class="dropdown-item">
                                    Login
                                </router-link>
                            </li>
                            <li>
                                <router-link to="/register" class="dropdown-item">
                                    Register
                                </router-link>
                            </li>
                        </template>
                    </ul>
                </li>

                <li class="nav-item mx-3">
                    <a
                        href="#"
                        class="nav-link"
                        type="button"
                        data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvasCart"
                        aria-controls="offcanvasCart"
                    >
                    <i class="bi bi-cart fs-1"></i>   
                    </a>
                </li>
            </ul>
        </div>
    </div>
  </nav>
</template>

<script>
    // export default {
    //     name: 'navbar',
    //     computed: {
    //         ...mapStores(useUserStore),
    //         ...mapWritableState(useUserStore, ['username']),
    //     },
    //     created(){
    //         this.getUsername()
    //     },
    //     methods: {
    //         async getUsername(){
    //            await axios
    //                 .get("api/v1/users/me",)
    //                 .then(response => {
    //                     this.username = response.data.username
    //                     console.log('logged in as ' + response.data.username)
    //                 })
    //                 .catch(error => {
    //                     console.log(error)
    //                 })  
    //         },
    //     }
    // }

</script>




<style scoped>

</style>
