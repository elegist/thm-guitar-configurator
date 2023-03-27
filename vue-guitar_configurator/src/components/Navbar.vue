<script setup>
import { useUserStore }  from '../stores/user'
import CartOffCanvas from "../components/cart/cart-offcanvas.vue"
import { mapStores } from 'pinia'
import axios from 'axios'
import { nextTick } from 'vue';
import {ref} from 'vue'

//const userStore = useUserStore()

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
                        Welcome Back, <span class="text-color-info">{{ userStore.username }}</span>
                        <a
                        @click="logout"
                        type="button"
                        class="mx-3 link-secondary"
                        >
                        Logout
                        </a>
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
    export default {
        name: 'navbar',
        data(){
            return{
                userStore: useUserStore(),
                username: ''
            } 
        },
        mounted() {
            if (this.userStore.isAuthenticated) {
                axios
                    .get("api/v1/users/me/")
                    .then(response => {
                        this.userStore.setUser(response.data.username) 
                        return response 
                    })
                    .then(response => this.userStore.setUserId(response.data.id))
                    .catch(error => console.log(error));
            }
        },
        methods: {
            logout(){
                axios.defaults.headers.common["Authorization"] = ""
                localStorage.removeItem("token")
                
                this.userStore.removeToken()
                this.userStore.removeUser()
                //this.$router.push('/')
            }
        }
    }

</script>




<style scoped>

</style>
