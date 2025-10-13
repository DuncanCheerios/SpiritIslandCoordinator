<!-- src/views/Home.vue -->
<template>
  <div class="home ">
    <h1 class="">Welcome to Spirit Island Coordinator</h1>

    <p class="">
      Organize your games, pick spirits, and track player progress.
    </p>

    <div class="">
      <router-link
        to="/games"
        class=""
      >
        View Active Games
      </router-link>
      <router-link
        to="/games/create"
        class=""
      >
        Create New Game
      </router-link>

    </div>

    <div class="">
      <button
        @click="logout"
        class=""
      >
        Logout
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const logout = () => {
  auth.logout()
  router.push('/login')
}
</script>

<style scoped>
.home p {
  color: #4b5563; /* gray-700 for Tailwind */
}
</style>
