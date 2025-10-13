<!-- src/components/GameCard.vue -->
<template>
  <div class="">
    <h3 class="">{{ game.name }}</h3>
    <p class="">
      Players: {{ game.players?.length ?? 0 }}
    </p>
    <button
      v-if="!joined"
      @click="joinGame"
      class=""
    >
      Join
    </button>
    <span v-else class="">Joined</span>
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
