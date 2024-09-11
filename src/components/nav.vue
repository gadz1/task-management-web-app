<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="top-nav">
    <div class="brand-logo">
      <RouterLink to="/">Task Manger</RouterLink>
    </div>
    <ul class="nav-links">
      <li><RouterLink to="/home">Projects</RouterLink></li>
      <li><RouterLink to="/tags">Tags</RouterLink></li>
      <li><RouterLink to="/members">Members</RouterLink></li>
    </ul>
  </nav>
</template>

<style scoped>
.top-nav {
  display: flex;  
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%; 
  background-color: #333;
  color: white;
  padding: 1rem;
  box-sizing: border-box;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
}

.brand-logo a{
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-links li {
  display: inline;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-size: 15px;
}

.nav-links a:hover {
  font-size:20px;
}
</style>