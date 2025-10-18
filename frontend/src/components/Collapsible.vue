<template>
  <div class="collapsible">
    <button class="toggle" @click="toggleOpen">
      {{ isOpen ? 'Hide' : 'Show' }} Events
    </button>

    <transition name="collapse">
      <div v-if="isOpen" class="content">
        <slot />
      </div>
    </transition>
  </div>
</template>

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
  max-height: 500px;
  opacity: 1;
}
</style>
