import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useLocalStorage } from "@vueuse/core";
import axios from "axios";

export const useUserStore = defineStore("user", {
    //state
    state: () => ({
        username: "",
        isAuthenticated: false,
        token: "",
    }),

    //getters

    actions: {
        init() {
            if (localStorage.getItem("token")) {
                this.token = localStorage.getItem("token");
                this.isAuthenticated = true;
            } else {
                this.token = "";
                this.isAuthentiated = false;
            }
        },
        setToken(token) {
            this.token = token;
            this.isAuthenticated = true;
        },
        removeToken() {
            this.token = "";
            this.isAuthenticated = false;
        },
        setUser(name) {
            this.username = name;
        },
    },
});
