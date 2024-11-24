<script setup lang="ts">
import type News from '@/models/News'
import { getTags } from '@/services/tagsService'
import { onMounted, useTemplateRef, defineEmits, ref, type Ref } from 'vue'
import { getNewsById } from '@/services/newsService'
import type Tag from '@/models/Tag'

const emits = defineEmits(['closeCardForm', 'saveCardForm'])
const props = defineProps({
  newsId: { type: String, required: true },
})

const modalRef = useTemplateRef('modal')
const selectedTag = ref(null)
const tags: Ref<Array<Tag>> = ref([])
const newsItem = ref<News>({
  uuid: '',
  text: '',
  title: '',
  created_at: '',
  updated_at: '',
  tags: {
    uuid: '',
    name: '',
  },
})

onMounted(async () => {
  document.body.style.overflow = 'hidden'
  if (modalRef.value) modalRef.value.style.top = `${window.scrollY + window.innerHeight * 0.25}px`
  newsItem.value = await getNewsById(props.newsId)
  selectedTag.value = newsItem.value.tags.uuid
  tags.value = await getTags()
})

const closeCard = () => {
  document.body.style.overflow = ''
  emits('closeCardForm', '')
}

const saveCard = () => {
  document.body.style.overflow = ''
  const currentTag = tags.value.find((x) => x.uuid === selectedTag.value)
  newsItem.value.tags = currentTag
  emits('saveCardForm', newsItem.value)
}
</script>

<template>
  <div
    class="block fixed z-10 bg-black opacity-75 left-0 top-0 w-full h-full"
    @click="closeCard"
  ></div>

  <div
    class="absolute z-20 bg-white w-1/3 px-4 pt-10 pb-6 rounded-md left-1/2 -translate-x-1/2 flex flex-col gap-y-4"
    ref="modal"
  >
    <button class="absolute right-3 top-3 text-3xl" title="Закрыть" @click="closeCard">
      <i class="fa-solid fa-xmark"></i>
    </button>

    <div>
      <h4 class="font-bold text-xl select-none">#Заголовок</h4>
      <input
        class="border hover:border-black focus:border-black transition-all outline-none rounded-md w-full placeholder:italic py-1 px-3"
        placeholder="Заголовок статьи..."
        type="text"
        v-model="newsItem.title"
      />
    </div>

    <div class="flex items-center gap-x-3">
      <h4 class="font-bold text-xl select-none">#Тег</h4>
      <select
        class="border py-1 px-2 rounded-md outline-none hover:border-black"
        v-model="selectedTag"
      >
        <option :value="tag.uuid" v-for="tag in tags">{{ tag.name }}</option>
      </select>
    </div>

    <div>
      <h4 class="font-bold text-xl select-none">#Текст</h4>
      <textarea
        class="placeholder:italic border hover:border-black focus:border-black transition-all outline-none rounded-md w-full py-1 px-3"
        rows="5"
        placeholder="Текст статьи..."
        v-model="newsItem.text"
      ></textarea>
    </div>

    <div>
      <button class="rounded-md bg-black text-white py-1 px-3" type="button" @click="saveCard">
        Сохранить
      </button>
    </div>
  </div>
</template>

<style>
textarea {
  resize: none;
}
</style>
