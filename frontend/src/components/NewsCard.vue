<script lang="ts" setup>
// types
import type { PropType } from 'vue'
import type News from '@/models/News'

const TEXT_MAX_LENGTH = 95

defineProps({
  news: { type: Object as PropType<News>, required: true },
})

const emits = defineEmits(['removeNews', 'showNews', 'editNews'])

const cropText = (text: string, maxLength: number): string => {
  return text.length > maxLength ? `${text.substring(0, maxLength - 3)}...` : text
}
</script>

<template>
  <div>
    <div
      class="border group px-4 py-6 rounded-md hover:border-black transition-all select-none flex overflow-hidden"
    >
      <div class="transition-all w-full">
        <h2 class="font-bold uppercase text-xl">{{ news.title }}</h2>
        <hr class="border-1 border-black mt-1 w-full"/>
        <div class="mt-2 font-medium">{{ news.date }} / {{ news.author }}</div>
        <p class="break-words mt-3">{{ cropText(news.text, TEXT_MAX_LENGTH) }}</p>
      </div>

      <div
        class="test flex flex-col opacity-0 justify-center ml-7 gap-y-3 transition-all invisible w-0 group-hover: group-hover:visible group-hover:w-fit group-hover:opacity-100"
      >
        <button
          class="bg-black text-white py-2 px-2.5 rounded-md"
          title="Открыть новость"
          @click="() => emits('showNews', news)"
        >
          <i class="fa-solid fa-magnifying-glass"></i>
        </button>
        <button
          class="bg-black text-white py-2 px-2.5 rounded-md"
          title="Редактировать новость"
          @click="() => emits('editNews', news)"
        >
          <i class="fa-solid fa-pen"></i>
        </button>
        <button
          class="bg-black text-white py-2 px-2.5 rounded-md"
          title="Удалить новость"
          @click="() => emits('removeNews', news.id)"
        >
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>
    </div>
  </div>
</template>
