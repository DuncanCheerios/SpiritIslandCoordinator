<template>
  <div class="event-list">
    <h3 class="title">Game Log</h3>
    <div class="event-container">
      <div v-for="(event, index) in events" :key="index" class="event-item">
        <div class="event-time">{{ event.time }}</div>
        <div class="event-text">{{ event.description }}</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface GameEvent {
  time: string
  description: string
}

const events = ref<GameEvent[]>([
  { time: '00:01', description: 'Game started' },
  { time: '00:05', description: 'Fear card drawn: Terror Spreads' },
  { time: '00:08', description: 'Event card revealed: Sudden Ambush' },
  { time: '00:12', description: 'Invader card played: Build in Wetlands' },
  { time: '00:15', description: 'Power used: Lightning’s Swift Strike' },
  { time: '00:18', description: 'Blight added to Jungle' },
  { time: '00:22', description: 'Fear card drawn: Dahan Defend the Island' },
  { time: '00:25', description: 'Event card revealed: Escalation!' },
  { time: '00:30', description: 'Invader card played: Explore in Mountains' },
])
</script>

<style scoped>
.event-list {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
  max-height: 300px; /* Adjust height as needed */
  overflow-y: auto;  /* Makes it scrollable */
  background-color: #fafafa;
}

.title {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
  font-weight: bold;
  border-bottom: 1px solid #ddd;
  padding-bottom: 0.25rem;
}

.event-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.event-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  background: white;
  border-radius: 4px;
  padding: 0.5rem;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.event-time {
  font-size: 0.8rem;
  color: #666;
  width: 60px;
}

.event-text {
  flex: 1;
}
</style>
