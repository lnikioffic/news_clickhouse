<script lang="ts" setup>
const emit = defineEmits(['createNews'])
</script>

<template>
  <header class="border-b py-4 select-none">
    <div class="container flex justify-between">
      <h1 class="text-3xl font-bold und">#CRUD News</h1>

      <button
        class="text-lg"
        type="button"
        title="Добавить новость"
        @click="() => emit('createNews', null)"
      >
        <i class="fa-solid fa-plus"></i>
      </button>
    </div>
  </header>
</template>
