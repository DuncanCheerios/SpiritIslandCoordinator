<!-- src/components/Register.vue -->
<template>
  <div class="max-w-sm mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Register</h2>
    <form @submit.prevent="submit">
      <input v-model="username" placeholder="Username" class="border p-2 w-full mb-3" />
      <input type="password" v-model="password" placeholder="Password" class="border p-2 w-full mb-3" />
      <button class="bg-green-500 text-white px-4 py-2 rounded w-full mb-3">Register</button>
    </form>
    <p class="text-sm text-gray-600">
      Already have an account?
      <router-link to="/login" class="text-blue-500 hover:underline">Login here</router-link>
    </p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const auth = useAuthStore()
const router = useRouter()

const submit = async () => {
  try {
    await auth.register(username.value, password.value)
    router.push('/')
  } catch (err) {
    alert('Registration failed')
  }
}
</script>
