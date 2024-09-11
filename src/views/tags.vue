<script setup>
import Nav from '../components/nav.vue';
import Add from '../components/add.vue';
import { ref, onMounted } from 'vue';

// Define a reactive variable to store the tags
const tags = ref([]);

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/tags', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    });

    if (response.ok) {
      const data = await response.json();
      tags.value = data;  // Store the tags in the reactive variable
    } else {
      console.error('Failed to fetch tags');
    }
  } catch (error) {
    console.error('Error fetching tags:', error);
  }
});
</script>

<template>
  <div class="contain">
    <Nav />
    <h1>tags</h1>
    <Add />
    <ul class="tag-list">
      <li v-for="tag in tags" :key="tag.id" class="tag-item">
        {{ tag.name }} 
        <span class="tag-color" :style="{ backgroundColor: tag.color }"></span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.contain {
  background-color: mistyrose;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  display: flex;  
  flex-direction: column;
  position: fixed;
  overflow-y: auto; /* Ensure content can scroll if it's too long */
}

h1 {
  margin: 20px 0; /* Space between the nav bar and the title */
  text-align: center;
}

.tag-list {
  padding: 0;
  margin: 20px;
  list-style-type: none; /* Remove bullets */
}

.tag-item {
  padding: 10px 15px;
  margin: 8px 0;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tag-color {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1px solid #ddd;
}
</style>

