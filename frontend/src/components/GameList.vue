<template>
  <div class="game-list p-4">
    <h2 class="text-2xl font-bold mb-4">Active Games</h2>

    <ul>
      <li
        v-for="game in games"
        :key="game.id"
        class="border rounded-md p-3 mb-2 hover:shadow-md transition"
      >
        <div class="flex justify-between items-center">
          <div>
            <h3 class="text-lg font-semibold">{{ game.name }}</h3>
<!--            <p class="text-sm text-gray-600">-->
<!--              {{ game.players.length }} player{{ game.players.length !== 1 ? 's' : '' }}-->
<!--            </p>-->
          </div>
          <button
            class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
            @click="$emit('join', game.id)"
          >
            Join
          </button>
        </div>
      </li>
    </ul>

    <div v-if="games && games.length === 0" class="text-gray-500 mt-4">
      No active games yet.
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../api/axios'

// const games = ref<Array<{ id: number; name: string; players: any[] }>>([])

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
.game-list li {
  cursor: pointer;
}
</style>
