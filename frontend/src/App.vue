<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent />
    <TournamentsList />
  </div>
</template>

<script>
import MyComponent from './components/MyComponent.vue'
import TournamentsList from './components/TournamentsList.vue'

export default {
  name: 'App',
  components: {
    MyComponent,
    TournamentsList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
