<template>
    <header>
        <nav class="container">
            <div class="branding">
                <RouterLink to="/">App</RouterLink>
            </div>
            <ul class="nav-routes">
                <RouterLink to="/">Home</RouterLink>
                <RouterLink to="/about">About</RouterLink>
                <RouterLink to="/smaa2">SMAA-2</RouterLink>
                <RouterLink to="/smaatri">SMAA-Tri</RouterLink>
            </ul>
        </nav>
    </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style lang="scss" scoped>
header {
    background-color: #f1f1f1;

    nav {
        display: flex;
        align-items: center;
        padding: 25px 16px;

        .branding {
            display: flex;
            align-items: center;
            gap: 8px;
            //   img {
            //     max-width: 50px;
            //   }

            a {
                font-size: 24px;
                text-decoration: none;
                color: inherit;
            }
        }

        .nav-routes {
            display: flex;
            flex: 1;
            justify-content: flex-end;
            gap: 12px;
            list-style: none;

            a {
                text-decoration: none;
                color: inherit;
            }
        }
    }
}
</style>