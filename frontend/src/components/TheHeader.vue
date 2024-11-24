<script lang="ts" setup>
const emit = defineEmits(['createNews', 'createTag'])
</script>

<template>
  <header class="border-b py-4 select-none">
    <div class="container flex justify-between">
      <h1 class="text-3xl font-bold und">#CRUD News</h1>

      <div class="flex gap-x-6">
        <button class="text-lg" type="button" title="Добавить тег" @click="() => emit('createTag')">
          <i class="fa-solid fa-plus"></i>
        </button>

        <button
          class="text-lg"
          type="button"
          title="Добавить новость"
          @click="() => emit('createNews')"
        >
          <i class="fa-solid fa-file-circle-plus"></i>
        </button>
      </div>
    </div>
  </header>
</template>
