<script setup lang="ts">
import type TagBase from '@/models/TagBase'
import { onMounted, useTemplateRef, defineEmits, reactive } from 'vue'

const emits = defineEmits(['closeCardForm', 'saveCardForm'])
const modalRef = useTemplateRef('modal')

const tag: TagBase = reactive({
  name: '',
})

onMounted(() => {
  document.body.style.overflow = 'hidden'
  if (modalRef.value) modalRef.value.style.top = `${window.scrollY + window.innerHeight * 0.25}px`
})

const closeCard = () => {
  document.body.style.overflow = ''
  emits('closeCardForm')
}

const saveCard = () => {
  document.body.style.overflow = ''
  emits('saveCardForm', tag)
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
      <h4 class="font-bold text-xl select-none">#Тег</h4>
      <input
        class="border hover:border-black focus:border-black transition-all outline-none rounded-md w-full placeholder:italic py-1 px-3"
        placeholder="Тег..."
        type="text"
        v-model="tag.name"
      />
    </div>

    <div>
      <button class="rounded-md bg-black text-white py-1 px-3" type="button" @click="saveCard">
        Сохранить
      </button>
    </div>
  </div>
</template>
