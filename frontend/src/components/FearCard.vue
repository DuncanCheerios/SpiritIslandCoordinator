<template>
  <div class="fear-card">
    <h4>{{ card.name }}</h4>
    <img v-if="card.image_url" :src="card.image_url" alt="" class="card-image" />
    <div class="stages">
      <p v-if="highlightStage === '1'" class="highlighted"><strong>Stage 1:</strong> {{ card.stage_one }}</p>
      <p v-if="highlightStage === '2'" class="highlighted"><strong>Stage 2:</strong> {{ card.stage_two }}</p>
      <p v-if="highlightStage === '3'" class="highlighted"><strong>Stage 3:</strong> {{ card.stage_three }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  card: {
    type: Object,
    required: true
  },
  highlightStage: {
    type: String, // 1, 2, or 3
    default: null
  }
})
</script>

<style scoped>
.fear-card {
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  background: #fafafa;
}

.card-image {
  display: block;
  margin: 0.5rem 0;

    /* OR for bigger responsive images, uncomment below */
  max-width: 100%;
  height: auto;
  object-fit: contain;
}


.stages p {
  margin: 0.25rem 0;
}

/* Highlight style */
.highlighted {
  font-weight: bold;
  background-color: #fff8c4;
  padding: 0.1rem 0.2rem;
  border-radius: 3px;
}
</style>
