import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';



axios.defaults.baseURL = process.env.VUE_APP_API_URL

const app = createApp(App)
app.config.globalProperties.$http = axios

app.use(VueSweetalert2);


app.mount('#app')
