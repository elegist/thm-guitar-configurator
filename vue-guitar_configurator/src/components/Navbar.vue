<script setup>

</script>

<template>
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
                    Hello, <span class="text-color-info">Guest</span>
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
                        <li>
                            <router-link to="/login" class="dropdown-item">
                                Login
                            </router-link>
                        </li>
                        <li>
                            <a href="#" class="dropdown-item"
                                >Register</a
                            >
                        </li>
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

<style scoped>

</style>
