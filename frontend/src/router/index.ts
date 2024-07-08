import { createRouter, createWebHistory } from 'vue-router'
import HomeRoute from '../components/HomeRoute.vue'
import PingRoute from '../components/PingRoute.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: PingRoute
    },
    {
      path: '/',
      name: 'Home',
      component: HomeRoute
    }
  ]
})

export default router
