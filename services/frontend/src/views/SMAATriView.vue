<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
    <header>
        <div>
            <h1>SMAA Tri</h1>
        </div>
    </header>
    <main>
        <nav>
            <ul class="nav_items">
                <RouterLink :to="{name: 'alt_smaatri'}">Alternatives</RouterLink>
                <RouterLink :to="{name: 'cat_smaatri'}">Categories</RouterLink>
                <RouterLink :to="{name: 'cri_smaatri'}">Criterions</RouterLink>
                <RouterLink :to="{name: 'pref_smaatri'}">Preference</RouterLink>
                <RouterLink :to="{name: 'lambda_smaatri'}">Lambda</RouterLink>
                <RouterLink :to="{name: 'results_smaatri'}">Result</RouterLink>
            </ul>
        </nav>
        <div class="list">
            <RouterView />
        </div>
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

.list {
  display: flex;
  flex-direction: column;
  max-width: 50%;
  width: 100%;
  margin: 0 auto;
  padding: 40px 16px;
}
</style>