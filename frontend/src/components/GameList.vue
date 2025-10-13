<template>
  <div class="game-list p-4">
    <h2 class="text-2xl font-bold mb-4">Active Games</h2>

    <ul>
      <GameCard
        v-for="game in games"
        :key="game.id"
        :game="game"
      >
      </GameCard>
    </ul>

    <div v-if="games && games.length === 0" class="text-gray-500 mt-4">
      No active games yet.
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../api/axios'
import GameCard from './GameCard.vue'


const games = ref<Array<{ id: number; name: string; players: any[] }>>([])

const fetchGames = async () => {
  try {
    const response = await api.get('games/')
    games.value = response.data
  } catch (err) {
    console.error('Failed to fetch games:', err)
  }
}

onMounted(() => {
  fetchGames()
})
</script>

<style scoped>
</style>
