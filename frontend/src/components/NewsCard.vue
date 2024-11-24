<script lang="ts" setup>
import { getDateString } from '@/services/dateHelper'
// types
import type { PropType } from 'vue'
import type News from '@/models/News'

const TEXT_MAX_LENGTH = 70
const TITLE_MAX_LENGTH = 17

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
      class="border group px-4 py-6 rounded-md hover:border-black transition-all select-none flex justify-between overflow-hidden"
    >
      <div class="transition-all" style="width: 83%">
        <h2 class="font-bold uppercase text-xl overflow-hidden whitespace-nowrap text-ellipsis">
          {{ news.title }}
        </h2>
        <hr class="border-1 border-black mt-1 w-full" />
        <div class="mt-2 font-medium">
          {{ getDateString(news.updated_at) }} / {{ news.tags.name }}
        </div>
        <p class="break-words mt-3">{{ cropText(news.text, TEXT_MAX_LENGTH) }}</p>
      </div>

      <div style="width: 15%" class="flex justify-end">
        <div class="flex flex-col justify-center gap-y-3 w-fit">
          <button
            class="bg-black text-white py-2 px-2.5 rounded-md"
            title="Открыть новость"
            @click="() => emits('showNews', news.uuid)"
          >
            <i class="fa-solid fa-magnifying-glass"></i>
          </button>
          <button
            class="bg-black text-white py-2 px-2.5 rounded-md"
            title="Редактировать новость"
            @click="() => emits('editNews', news.uuid)"
          >
            <i class="fa-solid fa-pen"></i>
          </button>
          <button
            class="bg-black text-white py-2 px-2.5 rounded-md"
            title="Удалить новость"
            @click="() => emits('removeNews', news.uuid)"
          >
            <i class="fa-solid fa-trash"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
