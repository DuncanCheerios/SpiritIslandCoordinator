<template>
  <div class="">
    <h1 class="">Game Details</h1>

    <!-- Game info placeholder -->
    <section class="">
      <h2 class="">Game Name</h2>
      <p class="">{{ game.name || 'Lorem Ipsum Game Name' }}</p>
    </section>

    <section class="">
      <h2 class="">Players</h2>
      <ul class="">
        <li v-for="player in game.players || placeholderPlayers" :key="player.username">
          {{ player.username }}
        </li>
      </ul>
    </section>

    <section class="">
      <h2 class="">Game Notes</h2>
      <p class="">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet lacus enim.
        Nulla facilisi. Suspendisse potenti. Integer ac nunc non nisi scelerisque dictum.
      </p>
    </section>

    <section>
      <h2 class="">Additional Info</h2>
      <p class="">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec ipsum a leo gravida
        tincidunt. Etiam vitae lorem non justo euismod tempus.
      </p>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../api/axios'

interface Player {
  username: string
}

interface Game {
  id: number
  name: string
  players: Player[]
}

// Route param to fetch game ID
const route = useRoute()
const gameId = Number(route.params.id)

const game = ref<Game>({
  id: gameId,
  name: '',
  players: [],
})

// Placeholder players for now
const placeholderPlayers = [
  { username: 'Alice' },
  { username: 'Bob' },
  { username: 'Charlie' },
]

// Optional: fetch game info from backend when ready
onMounted(async () => {
  // Uncomment when backend endpoint is available
  // const res = await api.get(`games/${gameId}/`)
  // game.value = res.data
  game.value.name = 'Lorem Ipsum Game Name'
  game.value.players = placeholderPlayers
})
</script>

<style scoped>
/* Optional additional styles */
</style>
