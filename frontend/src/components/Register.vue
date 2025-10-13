<!-- src/components/Register.vue -->
<template>
  <div class="">
    <h2 class="">Register</h2>
    <form @submit.prevent="submit">
      <input v-model="username" placeholder="Username" class="" />
      <input type="password" v-model="password" placeholder="Password" class="" />
      <button class="">Register</button>
    </form>
    <p class="">
      Already have an account?
      <router-link to="/login" class="">Login here</router-link>
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
