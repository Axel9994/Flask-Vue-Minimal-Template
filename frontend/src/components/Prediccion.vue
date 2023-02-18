<template>
    <div>
      <h1>Flask Vue Minimal Template</h1>
      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="numero">Número: </label>
          <input type="text" class="form-control" id="numero" name="numero" v-model="numero">
        </div>
        <br/>
        <button type="submit" class="btn btn-primary">Realizar predicción</button>
      </form>
      <div v-if="prediccion">
        <h2>Predicción:</h2>
        <p>{{ prediccion }}</p>
      </div>
    </div>
  </template>
  
  <script>

  export default {
    name: 'Prediccion-item',
    data() {
      return {
        numero: null,
        prediccion: null
      }
    },
    methods: {
      async onSubmit() {
        const response = await this.$http.post('/api/predict', { numero: this.numero })
        this.prediccion = response.data.response
      },
    },
  }
  </script>
  