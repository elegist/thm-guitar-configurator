import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useLocalStorage } from "@vueuse/core";
import axios from "axios";

export const useUserStore = defineStore("user", {
    //state
    state: () => ({
        username: "",
        userId: "",
        isAuthenticated: false,
        token: "",
    }),

    //getters

    actions: {
        init() {
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
        removeUser(){
            this.username = ""
        },
        setUserId(id){
            this.userId = id;
        },
        removeUserId(){
            this.userId = ""
        }
    },
    persist: true,
});
