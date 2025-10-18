<template>
  <div class="collapsible">
    <button class="toggle" @click="toggleOpen">
      {{ isOpen ? 'Hide' : 'Show' }}
    </button>

    <transition name="collapse">
      <div v-if="isOpen" class="content">
        <slot />
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isOpen = ref(true)
const toggleOpen = () => (isOpen.value = !isOpen.value)
</script>

<style scoped>
.collapse-enter-active,
.collapse-leave-active {
  transition: all 0.3s ease;
}
.collapse-enter-from,
.collapse-leave-to {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
}
.collapse-enter-to,
.collapse-leave-from {
  max-height: 500px; /* large enough to fit content */
  opacity: 1;
}
</style>
