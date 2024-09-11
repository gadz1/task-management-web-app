<script setup>
import { ref } from 'vue';

const formData = ref({
  name: '',
  color: ''
});

const createTag = async ()=>{
  const response = await fetch('http://127.0.0.1:5000/api/createTag', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData.value)
    });
};
</script>

<template>
  <h1>Create a Tag</h1>
  <form @submit.prevent="createTag">
  <div>
    <label for="name">Name:</label><br>
    <input type="text" id="name" v-model="formData.name" />
  </div>

  <div class="colors">
    <label for="color">Choose a color:</label><br>
    <select name="colors" id="colors" v-model="formData.color">
      <option value="red">Red</option>
      <option value="green">Green</option>
      <option value="blue">Blue</option>
    </select>
  </div>

  <button type="submit">Create Tag</button>
  </form>
</template>