<!-- src/components/GameCard.vue -->
<template>
  <div class="bg-white rounded-lg shadow p-4 border hover:shadow-lg transition">
    <h3 class="text-xl font-bold mb-2">{{ game.name }}</h3>
    <p class="text-gray-600 mb-2">
      Players: {{ game.players?.length ?? 0 }}
    </p>
    <button
      v-if="!joined"
      @click="joinGame"
      class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
    >
      Join
    </button>
    <span v-else class="text-green-500 font-semibold">Joined</span>
  </div>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue'
import api from '../api/axios'

interface Player {
  username: string
}

interface Game {
  id: number
  name: string
  players: Player[]
}

const props = defineProps<{
  game: Game
}>()

const joined = ref(false)

const joinGame = async () => {
  try {
    await api.post(`games/${props.game.id}/join/`) // backend endpoint
    joined.value = true
    props.game.players.push({ username: 'You' }) // simple client-side update
  } catch (err) {
    console.error(err)
    alert('Failed to join game')
  }
}
</script>

<style scoped>
/* optional hover/focus enhancements */
</style>
