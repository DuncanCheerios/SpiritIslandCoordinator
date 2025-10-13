<template>
  <div class="">
    <h2 class="">Create a New Game</h2>
    <form @submit.prevent="submit">
      <input
        v-model="gameName"
        placeholder="Game Name"
        class=""
      />
      <button class="">
        Create Game
      </button>
    </form>
    <p v-if="error" class="">{{ error }}</p>
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
