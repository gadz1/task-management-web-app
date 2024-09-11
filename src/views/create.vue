<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
const router = useRouter()
const formData=ref({
    name:'',
    describtion:''
});

const creatProject = async ()=>{
  const response = await fetch('http://127.0.0.1:5000/api/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData.value)
    });
};
</script>

<template>
  <div class="cont">
    <h1>Creat a new Project</h1>
    <form @submit.prevent="creatProject">
      <div>
      <label for="name">Name:</label><br>
      <input type="text" id="name" v-model="formData.name" />
      </div>

      <div>
      <label for="describtion">describtion:</label><br>
      <input type="text" id="describtion" v-model="formData.describtion" />
      </div>
      <br>
      <button type="submit">Creat Project</button>
    </form>
  </div>
</template>

<style scoped>
.cont {
  background-color: mistyrose;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  display: flex;  
  flex-direction: column;
  box-sizing: border-box;
  position: fixed;
}

input[type="text"] {
  width: 50%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 50px; 
}

.tag_box{
    margin-bottom: 20px;
    position: relative;
    display: inline-block;
    width: 50%;
}

select {
  width: 50%; /* Match the width of your text input for consistency */
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 50px;
  background-color: white; /* Ensure background color consistency */
  color: #333; /* Text color */
  font-size: 16px; /* Font size matching other form elements */
  appearance: none; /* Remove the default dropdown arrow */
  -webkit-appearance: none; /* Remove the default dropdown arrow for Safari */
  -moz-appearance: none; /* Remove the default dropdown arrow for Firefox */
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

form {
  margin-left: 10%;
}

button {  
  padding: 10px 20px;
  border-radius: 20px;
  color: white;
  background-color: coral;
  border: none;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

button:hover {
  background-color: darkorange;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

button:active {
  background-color: orangered;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transform: translateY(2px);
}
</style>
