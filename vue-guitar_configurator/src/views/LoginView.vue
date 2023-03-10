<template>
    <h1 class="py-4">Login</h1>

    <form class="row g-3 w-75 mx-auto p-3 border rounded" method='POST' action="">
        <div class="form-floating col-md-12">
            <input
                class="form-control"
                type="username"
                name="username"
                id="usernameInput"
                aria-describedby="usernameHelp"
                placeholder="Username"
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
            />
            <label for="passwordInput">Password</label>
        </div>
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-lg btn-success">Login</button>
        </div>
    </form>

    <p class="fw-light mt-2">Don't have an account yet? <i class="bi bi-arrow-right"></i> <a class="link-primary fw-bold" type="button" href="#">Register</a></p>

</template>


<script>
    export default {
        name: 'login',
        data() {
            return {}
        },
        components: {
            
        }
    }
</script>
<style>

</style>
