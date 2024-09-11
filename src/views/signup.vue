<script setup>
import { ref} from 'vue';
const formData = ref({
  mail: "",
  name:"",
  pass: ""
});

const handle = async () => {
    try {
    const response = await fetch('http://127.0.0.1:5000/api/signup', {
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
    <div class="container">
        <form @submit.prevent="handle">
            <div>
                <label for="email">Email: </label>
                <input type="email" v-model="formData.mail">
            </div>
            <div>
                <label for="name">User Name: </label>
                <input type="text" v-model="formData.name">
            </div>
            <div>
                <label for="pass">Password: </label>
                <input type="password" v-model="formData.pass">
            </div>
            <div>
                <label for="pass">Password: </label>
                <input type="password" v-model="formData.pass">
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<style scoped>
.container{
background-color: mistyrose;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  display: flex;  
  flex-direction: row;
  position: fixed;
  justify-content: center; 
  align-items: center;
}

input{
    width: 100%;
    padding: 5px;
    margin-bottom: 20px;
    border:none;
    border-radius: 10px;
}

button[type="submit"] {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}
</style>