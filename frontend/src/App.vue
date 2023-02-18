<template>
  <Prediccion ></Prediccion>
</template>

<script>
import Prediccion from './components/Prediccion.vue'

export default {
  name: 'App',
  components: {
    Prediccion
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
