<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const formData = ref({
  name: '',
  pass: ''
});

const handleSubmit = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData.value)  // Send the form data as JSON
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }

    const data = await response.json();
    console.log('Form submitted successfully:', data);
    
    if (data.message === 'Login successful') {
      router.push('/home');  // Redirect on successful login
    } else {
      alert('Invalid credentials');
    }
  } catch (error) {
    console.error('There was a problem with the form submission:', error);
  }
};
</script>

<template>
  <div class="cont">
    <div class="form-container">
      <form @submit.prevent="handleSubmit">

        <div>
          <label for="name">User Name:</label>
          <input type="text" id="name" v-model="formData.name" />
        </div>

        <div>
          <label for="pass">password:</label>
          <input type="password" id="pass" v-model="formData.pass" />
        </div>

        <button type="submit">Submit</button>
      </form>

      <button><RouterLink to="signup">sign up</RouterLink></button>

    </div>
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
  flex-direction: row;
  box-sizing: border-box;
  position: fixed;
}

.form-container {
  width: 40%;
  margin: 0 auto;
  padding: 1rem;
}

input[type="text"],
input[type="password"]{
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 50px; 
}

button {
  display: inline-block;
  padding: 10px 20px;
  margin-bottom: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>