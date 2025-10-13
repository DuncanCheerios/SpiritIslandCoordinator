<template>
  <div class="max-w-md mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Create a New Game</h2>
    <form @submit.prevent="submit">
      <input
        v-model="gameName"
        placeholder="Game Name"
        class="border p-2 w-full mb-3"
      />
      <button class="bg-green-500 text-white px-4 py-2 rounded w-full">
        Create Game
      </button>
    </form>
    <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import api from '../api/axios'
import { useRouter } from 'vue-router'

const gameName = ref('')
const error = ref('')
const router = useRouter()

const submit = async () => {
  if (!gameName.value) {
    error.value = 'Game name is required'
    return
  }

  try {
    await api.post('games/create/', { name: gameName.value })
    router.push('/games') // redirect to Game List
  } catch (err: any) {
    console.error(err)
    error.value = 'Failed to create game'
  }
}
</script>
