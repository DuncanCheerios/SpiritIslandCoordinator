<!-- src/views/Home.vue -->
<template>
  <div class="home max-w-3xl mx-auto mt-10 text-center">
    <h1 class="text-4xl font-bold mb-6">Welcome to Spirit Island Coordinator</h1>

    <p class="text-lg mb-8">
      Organize your games, pick spirits, and track player progress.
    </p>

    <div class="flex justify-center gap-4">
      <router-link
        to="/games"
        class="bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600 transition"
      >
        View Active Games
      </router-link>

      <router-link
        to="/games"
        class="bg-green-500 text-white px-6 py-3 rounded hover:bg-green-600 transition"
      >
        Create New Game
      </router-link>
    </div>

    <div class="mt-8">
      <button
        @click="logout"
        class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
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
