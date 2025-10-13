<template>
  <div class="min-h-screen bg-gray-100 text-gray-900">
    <!-- Global header -->
    <header class="bg-white shadow-md p-4">
      <div class="max-w-7xl mx-auto flex justify-between items-center">
        <h1 class="text-xl font-bold">Spirit Island Coordinator</h1>
        <div v-if="auth.isAuthenticated" class="text-gray-700">
          Logged in as <span class="font-semibold">{{ auth.user?.username }}</span>
        </div>
      </div>
    </header>

    <!-- Main content -->
    <main class="max-w-7xl mx-auto p-4">
      <router-view />
    </main>

    <!-- Optional footer -->
    <footer class="mt-auto bg-white text-center p-4 border-t text-gray-500">
      © 2025 Spirit Island Coordinator
    </footer>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from './stores/auth'

const auth = useAuthStore()
auth.checkAuth() // ensure user state is loaded on app start
</script>

<style>
/* optional global styles */
</style>
