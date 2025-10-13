// src/router.ts
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { useAuthStore } from './stores/auth'

import Home from './components/Home.vue'
import GameList from './components/GameList.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import CreateGame from './components/CreateGame.vue'

const routes: RouteRecordRaw[] = [
  {path: '/', name: 'Home', component: Home, meta: {requiresAuth: true}},
  {path: '/games', name: 'GameList', component: GameList, meta: {requiresAuth: true}},
  {path: '/login', name: 'Login', component: Login},
  {path: '/register', name: 'Register', component: Register},
  {path: '/:catchAll(.*)', redirect: '/'},
  {
    path: '/games/create',
    name: 'CreateGame',
    component: CreateGame,
    meta: {requiresAuth: true},
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  auth.checkAuth()
  if (to.meta.requiresAuth && !auth.isAuthenticated) next('/login')
  else if ((to.path === '/login' || to.path === '/register') && auth.isAuthenticated) next('/')
  else next()
})

export default router
