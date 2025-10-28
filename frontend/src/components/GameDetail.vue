<template>
  <div class="game-detail">
    <h2 v-if="game">{{ game.name }}</h2>
    <p v-else>Loading game...</p>

    <section v-if="game">
      <h3>Players:</h3>
      <ul>
        <li v-for="player in game.players" :key="player.id">
          {{ player.username }}
        </li>
      </ul>
    </section>

    <section>
      <Collapsible>
        <GameEventList :game-id="gameId"  />
      </Collapsible>
    </section>


    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../api/axios'
import GameEventList from "@/components/GameEventList.vue";
import Collapsible from "@/components/Collapsible.vue";

interface Player {
  id: number
  username: string
}

interface Game {
  id: number
  name: string
  players: Player[]
  created_at: string
}

const props = defineProps<{ gameId: string }>()

const game = ref<Game | null>(null)   // <-- reactive storage for the API result
const error = ref<string | null>(null)

onMounted(async () => {
  try {
    const res = await api.get(`games/${props.gameId}/`)
    game.value = res.data   // <-- store the result here
  } catch (err: any) {
    console.error(err)
    error.value = 'Failed to load game'
  }
})
</script>

<style scoped>
.error {
  color: red;
}
</style>
