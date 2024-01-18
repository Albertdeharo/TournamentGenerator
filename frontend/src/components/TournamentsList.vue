<template>
  <div>
    <h2>Listado de Torneos</h2>
    <ul>
      <li v-for="tournament in tournaments" :key="tournament.id">
        {{ tournament.name }} - {{ tournament.start_date }} to {{ tournament.end_date }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tournaments: [],
    };
  },
  mounted() {
    this.fetchTournaments();
  },
  methods: {
    async fetchTournaments() {
      try {
        const response = await axios.get('/api/tournaments/');
        this.tournaments = response.data.tournaments;
      } catch (error) {
        console.error('Error fetching tournaments:', error);
      }
    },
  },
};
</script>

<style>
/* Puedes agregar estilos según sea necesario */
</style>
