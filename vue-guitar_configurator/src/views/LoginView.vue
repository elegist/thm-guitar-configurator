<script setup>
    import axios from 'axios';
    import { mapStores } from 'pinia'

    //import { getAPI } from '../axios'
    //const userStore = useUserStore()
</script>

<template>
    <h1 class="py-4">Login</h1>

    <form @submit.prevent="login" class="row g-3 w-75 mx-auto p-3 border rounded">
        <div class="form-floating col-md-12">
            <input
                class="form-control"
                type="username"
                name="username"
                id="usernameInput"
                aria-describedby="usernameHelp"
                placeholder="Username"
                v-model="username"
            />
            <label for="usernameInput">User Name</label>
        </div>
        <div class="form-floating col-md-12">
            <input
                class="form-control"
                type="password"
                name="password"
                id="passwordInput"
                placeholder="Password"
                v-model="password"
            />
            <label for="passwordInput">Password</label>
        </div>
        <div class="d-grid gap-2">
            <button class="btn btn-lg btn-success">Login</button>
        </div>
    </form>

    <p class="fw-light mt-2">Don't have an account yet? <i class="bi bi-arrow-right"></i> <a class="link-primary fw-bold" type="button" href="#">Register</a></p>

</template>


<script>
    import { useUserStore } from '../stores/user';
    export default {
        name: 'login',
        // setup() {
        //     const userStore = useUserStore()
        //     const token = userStore.token
        //     return { userStore }
        // },
        data() {
            return {
                username: '',
                password: '',
            }
        },
        computed: {
            ...mapStores(useUserStore),
        },
        methods: {
            async login() {
                axios.defaults.headers.common["Authorization"] = ""
                localStorage.removeItem("token")

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                        .post("api/v1/token/login", formData)
                        .then(response => {
                            const token = response.data.auth_token
                            console.log(token)
                            this.userStore.setToken(token)

                            axios.defaults.headers.common["Authorization"] = "Token" + token
                            localStorage.setItem("token", token)
                            
                            this.$router.push('/')
                        })
                        .catch(error => {
                            console.log(error)
                        })
            }
            
        },
    }
</script>

<style>

</style>
