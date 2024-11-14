<script setup lang="ts">
import { onMounted, useTemplateRef } from 'vue'
// types
import type { PropType } from 'vue'
import type News from '@/models/News'

const emits = defineEmits(['closeCardForm'])
defineProps({
  news: { type: Object as PropType<News | null>, required: true },
})

const modalRef = useTemplateRef('modal')

onMounted(() => {
  document.body.style.overflow = 'hidden'
  if (modalRef.value) modalRef.value.style.top = `${window.scrollY + window.innerHeight * 0.25}px`
})

const closeCard = () => {
  document.body.style.overflow = ''
  emits('closeCardForm', null)
}
</script>

<template>
  <div class="block fixed z-10 bg-black opacity-75 left-0 top-0 w-full h-full" @click="closeCard"></div>

  <div
    class="absolute z-20 bg-white w-1/3 px-4 pt-10 pb-6 rounded-md left-1/2 -translate-x-1/2"
    ref="modal"
  >
    <button class="absolute right-2 top-2 text-3xl" title="Закрыть" @click="closeCard">
      <i class="fa-solid fa-xmark"></i>
    </button>

    <h2 class="font-bold uppercase text-xl">
      {{ news?.title }}
    </h2>
    <hr class="border-1 border-black mt-1" />
    <div class="mt-2 font-medium">{{ news?.date }} / {{ news?.author }}</div>

    <div class="max-h-96 overflow-auto mt-4">
      <p class="break-words">
        {{ news?.text }}
      </p>
    </div>
  </div>
</template>

<style></style>
