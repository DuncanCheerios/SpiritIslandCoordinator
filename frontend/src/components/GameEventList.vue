<template>
  <div class="game-events">
    <h2>Game Events</h2>

    <!-- List of events -->
    <div v-if="events.length" class="event-list">
      <div
        v-for="event in events"
        :key="event.id"
        @click="toggleCollapse(event)"
        class="event-card"
        style="cursor: pointer;"
      >
        <div class="event-header">
          <strong>{{ event.typeLabel }} - {{ event.title }}</strong>
          <span style="float: right;">{{ event.collapsed ? '+' : '–' }}</span>
        </div>
        <div v-show="!event.collapsed" class="event-content">
          <span v-if="event.fear_card">{{ event.fear_card.name }}
            <FearCard :card=event.fear_card :highlight-stage="event.terror_level "/>
          </span>

          <span v-else-if="event.event_card">{{ event.event_card.name }}</span>
          <span v-else-if="event.invader_card">{{event.description}} at {{ event.invader_card.name }}</span>
          <span v-else>{{ event.title }}</span>
          <small class="timestamp">({{ formatDate(event.created_at) }})</small>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No events yet.</p>
    </div>

    <hr />

    <!-- Add new event -->
    <h3>Add Event</h3>
    <form @submit.prevent="createEvent">
      <label>Type:</label>
      <select v-model="newEvent.type" required>
        <option disabled value="">Select type</option>
        <option value="fear">Fear Card</option>
        <option value="event">Event Card</option>
        <option value="invader">Invader Card</option>
        <option value="custom">Custom</option>
      </select>

      <!-- Fear Card select -->
      <div v-if="newEvent.type === 'fear'">
        <label>Fear Card:</label>
        <select v-model="newEvent.fear_card_id" required>
          <option disabled value="">Select card</option>
          <option
            v-for="card in fearCards"
            :key="card.id"
            :value="card.id"
          >
            {{ card.name }}
          </option>
        </select>
        <select v-model="newEvent.terror_level" id="stage">
          <option v-for="s in [1, 2, 3]" :key="s" :value="s">
            Terror Level {{ s }}
          </option>
        </select>
      </div>

      <!-- Event Card select -->
      <div v-if="newEvent.type === 'event'">
        <label>Event Card:</label>
        <select v-model="newEvent.event_card_id" required>
          <option disabled value="">Select card</option>
          <option
            v-for="card in eventCards"
            :key="card.id"
            :value="card.id"
          >
            {{ card.name }}
          </option>
        </select>
      </div>

      <!-- Event Card select -->
      <div v-if="newEvent.type === 'invader'">
        <label>Invader Action:</label>
        <select v-model="newEvent.invader_card_id" required>
          <option disabled value="">Select card</option>
          <option
            v-for="card in invaderCards"
            :key="card.id"
            :value="card.id"
          >
            {{ card.name }}
          </option>
        </select>
        <label>Description:</label>
        <textarea v-model="newEvent.description" placeholder="Ravage/Build/Explore/Etc" />
      </div>

      <!-- Custom Event -->
      <div v-if="newEvent.type === 'custom'">
        <label>Title:</label>
        <input v-model="newEvent.title" placeholder="Custom event title" />
        <label>Description:</label>
        <textarea v-model="newEvent.description" placeholder="Describe what happened..." />
      </div>

      <button type="submit" :disabled="isSubmitting">Add</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import api from "@/api/axios.js";
import FearCard from "@/components/FearCard.vue";

// Props
const props = defineProps({
  gameId: {
    type: Number,
    required: true,
  },
})

const events = ref([])
const fearCards = ref([])
const eventCards = ref([])
const invaderCards = ref([])
const isSubmitting = ref(false)

// New event data
const newEvent = ref({
  type: '',
  fear_card_id: null,
  event_card_id: null,
  invader_card_id: null,
  terror_level: null, // 1,2,3
  title: '',
  description: '',
})

// Load all data on mount
onMounted(async () => {
  await Promise.all([
    loadEvents(),
    loadFearCards(),
    loadEventCards(),
    loadInvaderCards(),
  ])
})

async function loadEvents() {
  const { data } = await api.get(`/games/${props.gameId}/events/`)
  events.value = data.map(e => ({
    ...e,
    typeLabel: e.type.charAt(0).toUpperCase() + e.type.slice(1),
    collapsed: true
  }))
}

function toggleCollapse(event) {
  event.collapsed = !event.collapsed
}

async function loadFearCards() {
  const { data } = await api.get('/fearcards/')
  fearCards.value = data
}

async function loadEventCards() {
  const { data } = await api.get('/eventcards/')
  eventCards.value = data
}

async function loadInvaderCards() {
  const { data } = await api.get('/invadercards/')
  invaderCards.value = data
}

async function createEvent() {
  isSubmitting.value = true
  try {
    const payload = { type: newEvent.value.type }

    if (newEvent.value.type === 'fear') {
      payload.fear_card_id = newEvent.value.fear_card_id
      payload.terror_level = newEvent.value.terror_level
    } else if (newEvent.value.type === 'event') {
      payload.event_card_id = newEvent.value.event_card_id
    } else if (newEvent.value.type === 'invader') {
      payload.invader_card_id = newEvent.value.invader_card_id
      payload.description = newEvent.value.description
    } else {
      payload.title = newEvent.value.title
      payload.description = newEvent.value.description
    }

    await api.post(`/games/${props.gameId}/events/`, payload)
    await loadEvents()
    resetForm()
  } finally {
    isSubmitting.value = false
  }
}

function resetForm() {
  newEvent.value = {
    type: '',
    fear_card_id: null,
    event_card_id: null,
    invader_card_id: null,
    terror_level: null,
    title: '',
    description: '',
  }
}

function formatDate(isoString) {
  const d = new Date(isoString)
  return d.toLocaleString()
}
</script>

<style scoped>
.game-events {
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
}
.event-list {
  max-height: 1000px;
  overflow-y: auto;
  margin-bottom: 1rem;
}
.event-card {
  background: #fafafa;
  padding: 0.5rem;
  border-radius: 6px;
  margin-bottom: 0.5rem;
  border: 1px solid #eee;
}
.timestamp {
  color: #666;
  font-size: 0.8em;
  margin-left: 0.5rem;
}
form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
select,
input,
textarea {
  padding: 0.4rem;
  font-size: 0.9rem;
}
button {
  align-self: start;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>
