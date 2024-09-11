<script setup>
import Nav from '../components/nav.vue'
import Add from '../components/add.vue'
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue';

const projs = ref([]);

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/getprojects', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    });

    if (response.ok) {
      const data = await response.json();
      projs.value = data;  
    } else {
      console.error('Failed to fetch projs');
    }
  } catch (error) {
    console.error('Error fetching projs:', error);
  }
});
</script>

<template>
  <div class="container">
    <Add />
    <Nav />
    <div class="projs">
      <h2>Projects</h2>
      <ul class="tag-list">
        <RouterLink to="/project">
        <li v-for="proj in projs" :key="proj.id" class="projs-item">
          {{ proj.name }} 
        </li>
        </RouterLink>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.container {
  background-color: aliceblue;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: row;
  position: fixed;
  margin-top: 55px;
}

.projs {
  margin-top: 2%;
  width: 100%;
  height: 85%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.tag-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap; /* Allow items to wrap if necessary */
  justify-content: center;
  gap: 20px; /* Add space between each project */
}

.projs-item {
  background-color: cornflowerblue;
  color: white;
  width: 150px; /* Fixed width for square */
  height: 150px; /* Fixed height to make it square */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  transition: transform 0.3s ease, background-color 0.3s ease;
  cursor: pointer;
}

.projs-item:hover {
  background-color: royalblue;
  transform: scale(1.05);
}
</style>
