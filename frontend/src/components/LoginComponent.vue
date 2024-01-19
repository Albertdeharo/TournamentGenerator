<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://localhost:8000/auth/login/', {
            username: this.username,
            password: this.password,
          });
  
          // Manejar la respuesta exitosa, almacenar el token, etc.
          console.log('Login exitoso:', response.data);
  
          // Redirigir a otra página, actualizar el estado de Vuex, etc.
        } catch (error) {
          // Manejar errores de autenticación
          console.error('Error de autenticación:', error.response.data);
        }
      },
    },
  };
  </script>
  