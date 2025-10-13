<template>
  <div class="">
    <!-- Global header -->
    <header class="">

      <!-- Navigation Bar -->
      <nav class="navbar">
        <div class="nav-left">
          <router-link to="/" class="nav-brand">Spirit Island Coordinator</router-link>
          <router-link to="/games" class="nav-link">Games</router-link>
          <router-link to="/games/create" class="nav-link">Create Game</router-link>
        </div>
        <div class="nav-right">
          <template v-if="auth.isAuthenticated">
            <span class="nav-user">Hello, {{ auth.user?.username }}</span>
            <button class="nav-button" @click="auth.logout">Logout</button>
          </template>
          <template v-else>
            <router-link to="/login" class="nav-link">Login</router-link>
            <router-link to="/register" class="nav-link">Register</router-link>
          </template>
        </div>
      </nav>
    </header>

    <!-- Main content -->
    <main class="">
      <router-view />
    </main>

    <!-- Optional footer -->
    <footer class="">
      © 2025 Spirit Island Coordinator
    </footer>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from './stores/auth'

const auth = useAuthStore()
auth.checkAuth()
</script>

<style scoped>
/* Navbar styling */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #222;
  padding: 12px 24px;
  color: white;
}

.nav-left, .nav-right {
  display: flex;
  align-items: center;
}

.nav-brand {
  font-weight: bold;
  font-size: 1.2rem;
  margin-right: 20px;
  color: white;
  text-decoration: none;
}

.nav-link {
  margin-right: 15px;
  color: white;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}

.nav-user {
  margin-right: 10px;
}

.nav-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
}

.nav-button:hover {
  background-color: #0056b3;
}

/* Main content area */
.main-content {
  padding: 20px;
}
</style>
