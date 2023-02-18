import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"


axios.defaults.baseURL = process.env.VUE_APP_API_URL

const app = createApp(App)
app.config.globalProperties.$http = axios


app.mount('#app')
