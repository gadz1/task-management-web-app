<script setup>
import { RouterLink, useRoute } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();

const destinationRoute = computed(() => {
  if (route.name === 'home') {
    return '/create';
  } else if(route.name === 'projectTemp') {
    return '/addTask';
  } else {
    return '/createtags';
  }
});
</script>

<template>
  <button class="butt">
    <RouterLink :to="destinationRoute">+</RouterLink>
  </button>
</template>

<style scoped> 
.butt {
    border-radius: 50px;
    background-color: cornflowerblue;
    width: 100px; 
    height: 100px; 
    border: none;
    cursor: pointer;
    position: fixed; 
    right: 50px;    
    bottom: 50px;
}

.butt a {
    color: white;
    font-size: 24px;
    text-decoration: none;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
</style>
