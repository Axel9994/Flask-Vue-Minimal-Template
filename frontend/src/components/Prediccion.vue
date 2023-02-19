<template>
    <div class="container">
      <h1>Flask Vue Minimal Template</h1>
      <br/>
      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="numero">Número: </label>
          <input type="text" class="form-control" id="numero" name="numero" v-model="numero">
        </div>
        <br/>
        <button type="submit" class="btn btn-primary">Realizar predicción</button>
      </form>
      <br />
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
        this.$http.post('/api/predict', { numero: this.numero })
          .then(response => this.prediccion = response.data.response)
          .catch(error => this.$swal({
            title: 'Error',
            text: error.response.data.message,
            icon: 'error',
            confirmButtonText: 'Aceptar'
          }))
        //this.prediccion = response.data.response
      },
    },
  }
  </script>
  