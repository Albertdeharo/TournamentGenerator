<template>
  <div>
    <h1>Lista de Proyectos</h1>
    <ul>
      <li v-for="project in projects" :key="project.id">{{ project.name }} - {{ project.website }} - {{ project.foundation }}</li>
      <!-- Ajusta las propiedades de tu objeto 'project' según la respuesta de tu API -->
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      projects: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/api/companies/');  // Reemplaza 'URL_DE_TU_API' con la URL correcta de tu API
        console.log(response.data)
        this.projects = response.data.companies;
      } catch (error) {
        console.error('Error al obtener proyectos:', error);
      }
    },
  },
};
</script>

<style>
/* Puedes agregar estilos CSS aquí si es necesario */
</style>
