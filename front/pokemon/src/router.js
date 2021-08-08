import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/pages/Home.vue'
import PageNotFound from '@/pages/PageNotFound.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'index', component: Home},
    { path: '/:notFound(.*)', name: 'notFound',component: PageNotFound } // Error
  ]
})

export default router