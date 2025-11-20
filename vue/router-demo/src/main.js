import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router'

 router.beforeEach((to,from, next)=>{
    if(to.path === "/login"){
         return next()
     }
    const token =localStorage.getItem("token")
    // console.log(token);
    if (!token) {
         return next("/login")
    }
     next()
 })

createApp(App).use(router).mount('#app')
