import { createRouter, createWebHistory } from 'vue-router';
import LoginComponent from './../components/LoginComponent.vue';
import TournamentsList from './../components/TournamentsList.vue';

const routes = [
  { path: '/login', component: LoginComponent },
  { path: '/tournaments', component: TournamentsList },
  // Otras rutas
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
