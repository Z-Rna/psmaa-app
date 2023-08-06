<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AboutHeader from '../components/AboutHeader.vue';
</script>

<template>
  <header class="header">
    <div>
      <AboutHeader />
    </div>
  </header>
  <main>
    <nav>
      <ul class="nav_items">
        <RouterLink :to="{name: 'about_project'}">Project</RouterLink>
        <RouterLink :to="{name: 'about_smaa2'}">SMAA-2</RouterLink>
        <RouterLink :to="{name: 'about_smaatri'}">SMAA-Tri</RouterLink>
      </ul>
    </nav>
    <RouterView/>
  </main>
</template>

<style lang="scss" scoped>
  nav {
    display: flex;
    align-items: center;
    padding: 25px 16px;
    .nav_items {
      display: flex;
      flex: 1;
      justify-content: center;
      gap: 12px;
      list-style: none;

      a {
          text-decoration: none;
          color: inherit;
      }
    }
  }

  main {
    text-align: center;
  }
</style>
