<script setup>
    import axios from 'axios'
    import { mapStores } from 'pinia'
</script>

<template>
    <h1 class="py-4">Register</h1>

    <form @submit.prevent="register" class="row g-3 w-75 mx-auto p-3 border rounded">
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
            <label for="usernameInput">Username</label>
        </div>
        <div class="form-floating col-md-12">
            <input
                class="form-control"
                type="email"
                name="email"
                id="emailInput"
                placeholder="Email"
                v-model="email"
            />
            <label for="emailInput">Email</label>
        </div>
        <div class="form-floating col-md-6">
            <input
                class="form-control"
                type="password"
                name="password1"
                id="password1Input"
                placeholder="Choose a password"
                v-model="password1"
            />
            <label for="password1Input">Choose a password</label>
        </div>
        <div class="form-floating col-md-6">
            <input
                class="form-control"
                type="password"
                name="password2"
                id="password2Input"
                placeholder="Repeat the password"
                v-model="password2"
            />
            <label for="password2Input">Repeat the password</label>
        </div>

        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-lg btn-success">Register</button>
        </div>
    </form>

    <p class="fw-light mt-2">Already have an account? <i class="bi bi-arrow-right"></i> <router-link class="link-primary fw-bold" type="button" to="/login">Login</router-link></p>

</template>

<script>
    export default {
        name: 'register',
        data() {
            return {
                username: '',
                email: '', //can be blank
                password1: '',
                password2: '',
                errors: [], //TODO: show erros to user
            }
        },
        methods: {
            register() {

                if (this.username === ''){
                    this.errors.push('Username is missing')
                }

                if(this.password1 === ''){
                    this.errors.push('Password is missing')
                }
                
                if(this.password1 !== this.password2){
                    this.errors.push('Passwords do not match')
                }


                if(!this.errors.length){
                    const formData = {
                        username: this.username,
                        email: this.email,
                        password: this.password1
                    }

                    axios
                        .post("api/v1/users/", formData)
                        .then(response => { 
                            this.$router.push('/login')
                            return response
                        })
                        .then(response => {
                            axios.post("api/v1/customer/", { user: response.data.id })
                        })
                        .catch(error => {
                            console.log(error)
                        })
                }
            }
        },
    }
</script>



<style>

</style>
