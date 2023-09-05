<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="header">
    <div>
      <h1>SMAA</h1>
    </div>
  </header>
  <main>
    <nav>
      <ul class="nav_items">
        <RouterLink :to="{ name: 'about_project' }">Project</RouterLink>
        <RouterLink :to="{ name: 'about_smaa2' }">SMAA-2</RouterLink>
        <RouterLink :to="{ name: 'about_smaatri' }">SMAA-Tri</RouterLink>
      </ul>
    </nav>
    <RouterView />
  </main>
</template>

<style lang="scss" scoped>
h1 {
  text-align: center;
  padding: 25px;
}

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
