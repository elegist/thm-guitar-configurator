<script setup>
import axios from "axios";
import { mapStores } from "pinia";
import SavedPresetCard from "../components/account/Saved-Preset-Card.vue";
//import { getAPI } from '../axios'
//const userStore = useUserStore()
</script>

<template>
    <section class="account-information pt-3">
        <h2 class="p-3">Account Information</h2>
        <form
            @submit.prevent="updateUser"
            class="row g-3 w-75 mx-auto p-3 border rounded"
        >
            <div class="form-floating col-xl-6">
                <input
                    class="form-control"
                    type="text"
                    name="username"
                    id="usernameInput"
                    aria-describedby="usernameHelp"
                    placeholder="Username"
                    v-model="username"
                />
                <label for="usernameInput">Username</label>
            </div>
            <div class="form-floating col-xl-6">
                <input
                    class="form-control"
                    type="email"
                    name="email"
                    id="emailInput"
                    aria-describedby="emailHelp"
                    placeholder="Email"
                    v-model="email"
                />
                <label for="emailInput">Email</label>
            </div>
            <div class="form-floating col-xl-12">
                <input
                    class="form-control"
                    type="text"
                    name="firstName"
                    id="first_nameInput"
                    aria-describedby="firstNameHelp"
                    placeholder="First Name"
                    v-model="firstName"
                />
                <label for="first_nameInput">First Name</label>
            </div>
            <div class="form-floating col-xl-12">
                <input
                    class="form-control"
                    type="text"
                    name="lastName"
                    id="last_nameInput"
                    aria-describedby="lastNameHelp"
                    placeholder="Last Name"
                    v-model="lastName"
                />
                <label for="last_nameInput">Last Name</label>
            </div>
            <div class="form-floating col-xl-12">
                <input
                    class="form-control"
                    type="text"
                    name="street"
                    id="streetInput"
                    aria-describedby="streetHelp"
                    placeholder="Street"
                    v-model="street"
                />
                <label for="streetInput">Street</label>
            </div>
            <div class="form-floating col-xl-5">
                <input
                    class="form-control"
                    type="text"
                    name="city"
                    id="cityInput"
                    aria-describedby="cityHelp"
                    placeholder="City"
                    v-model="city"
                />
                <label for="cityInput">City</label>
            </div>
            <div class="form-floating col-xl-5">
                <input
                    class="form-control"
                    type="text"
                    name="state"
                    id="stateInput"
                    aria-describedby="stateHelp"
                    placeholder="State"
                    v-model="state"
                />
                <label for="stateInput">State</label>
            </div>
            <div class="form-floating col-xl-2">
                <input
                    class="form-control"
                    type="text"
                    name="zipCode"
                    id="zip_codeInput"
                    aria-describedby="zipCodeHelp"
                    placeholder="Zip Code"
                    v-model="zipCode"
                />
                <label for="zip_codeInput">Zip Code</label>
            </div>

            <div class="d-grid gap-2">
                <button type="submit" class="btn btn-lg btn-success">
                    Update Information
                </button>
            </div>
        </form>
    </section>

    <section class="saved-presets pt-3">
        <h2 class="p-3">Saved Presets</h2>
        <div class="row">
            <div v-for="(configuration, id) in userConfigurations" :key="id" class="col-md-8 col-lg-4 my-2">
                <SavedPresetCard :configuration="configuration" :id="id" :items="items"/>
            </div>
        </div>
    </section>
</template>

<script>
import { useUserStore } from "../stores/user";
export default {
    name: "account",
    data() {
        return {
            userStore: useUserStore(),
            userConfigurations: [],
            items: [],
            username: "",
            email: "",
            firstName: "",
            lastName: "",
            street: "",
            city: "",
            state: "",
            zipCode: "",
        };
    },
    methods: {
        updateUser(){

            if (this.userStore.isAuthenticated){
                const customerFormData = {
                    first_name: this.firstName,
                    last_name: this.lastName,
                    street: this.street,
                    city: this.city,
                    state: this.state,
                    zip_code: this.zipCode,
                }

                const userFormData = {
                    username: this.username,
                    email: this.email,
                }

                axios
                    .put(`api/v1/customer/${this.userStore.userId}`, customerFormData)
                    .then(response => {
                        console.log(response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                axios
                    .put(`api/v1/user/${this.userStore.userId}`, userFormData)
                    .then(response => {
                        console.log(response.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.userStore.setUser(this.username)        
                }     
        },
    },
    created() {
        axios
            .get(`api/v1/user/${this.userStore.userId}`)
            .then(response => {
                this.username = response.data.username
                this.email = response.data.email
            })
            .catch(error => {
                console.log(error)
            })

        axios
            .get(`/api/v1/customer/${this.userStore.userId}`)
            .then(response => {
                console.log("customer", response.data.id)
                this.firstName = response.data.first_name
                this.lastName = response.data.last_name
                this.street = response.data.street
                this.city = response.data.city
                this.state = response.data.state
                this.zipCode = response.data.zip_code
                return response.data.id;
            })
            .then(response => {
                axios
                    .get(`/api/v1/configuration/${response}`)
                    .then(response => {
                        this.userConfigurations = response.data
                    })
            })
            .catch((error) => console.log(error))
        
        axios
            .get("/api/v1/item/")
            .then((response) => {
                console.log("data fetch from API successful -> Items");
                this.items = response.data;
            })
            .catch((error) => {
                console.log(error)
            });
    },
};
</script>

<style></style>
