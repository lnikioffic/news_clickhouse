<script lang="ts" setup>
// vue
import { ref, onMounted, type Ref } from 'vue'
// components
import Header from './components/TheHeader.vue'
import NewsCard from '@/components/NewsCard.vue'
import CreateNewsCardForm from './components/CreateNewsCardForm.vue'
import ShowNewsCardForm from '@/components/ShowNewsCardForm.vue'
import EditNewsCardForm from '@/components/EditNewsCardForm.vue'
//services
import { getNews, createNews, remoeNews, updateNews } from '@/services/newsService'
// types
import type News from '@/models/News'
import type NewsBase from './models/NewsBase'

// refs
const newsArr: Ref<Array<News>> = ref([])

onMounted(async () => {
  newsArr.value = await getNews()
})

//create form
const isVisibleCreateNewsCardForm: Ref<boolean> = ref(false)

const onCreateNewsFormVisible = () => {
  isVisibleCreateNewsCardForm.value = !isVisibleCreateNewsCardForm.value
}

const onCreateNewsItem = async (newsItem: NewsBase) => {
  const newNews: News = await createNews(newsItem)
  newsArr.value.push(newNews)
  onCreateNewsFormVisible()
}

//show form
const isVisibleShowNewsCardForm: Ref<boolean> = ref(false)
const showNewsItemId: Ref<string> = ref('')

const onShowNewsItem = (newsItemId: string) => {
  showNewsItemId.value = newsItemId
  isVisibleShowNewsCardForm.value = !isVisibleShowNewsCardForm.value
}

// remove
const onRemoveNewsItem = async (id: string) => {
  await remoeNews(id)
  const newsIdx = newsArr.value.findIndex((x) => x.uuid === id)
  newsArr.value.splice(newsIdx, 1)
}

// edit form
const isVisibleEditNewsCardForm: Ref<boolean> = ref(false)
const editNewsItemId: Ref<string> = ref('')

const onEditNewsFormVisible = (newsItemId: string) => {
  editNewsItemId.value = newsItemId
  isVisibleEditNewsCardForm.value = !isVisibleEditNewsCardForm.value
}

const onEditNewsItem = async (newsItem: News) => {
  const updatedNewsItem = await updateNews(newsItem)
  const newsIdx = newsArr.value.findIndex((x) => x.uuid === newsItem.uuid)
  newsArr.value[newsIdx] = updatedNewsItem
  onEditNewsFormVisible('')
}
</script>
<template>
  <Header @createNews="onCreateNewsFormVisible"></Header>

  <div class="container mt-16">
    <div>
      <h1 class="font-bold text-center text-4xl select-none">#ОСНОВНЫЕ НОВОСТИ</h1>

      <div class="mt-16 mb-20 grid grid-cols-3 gap-y-10 gap-x-14">
        <NewsCard
          v-for="newsItem in newsArr"
          :key="newsItem.uuid"
          :news="newsItem"
          @removeNews="onRemoveNewsItem"
          @showNews="onShowNewsItem"
          @editNews="onEditNewsFormVisible"
        ></NewsCard>
      </div>
    </div>

    <CreateNewsCardForm
      v-if="isVisibleCreateNewsCardForm"
      @saveCardForm="onCreateNewsItem"
      @closeCardForm="onCreateNewsFormVisible"
    ></CreateNewsCardForm>

    <ShowNewsCardForm
      v-if="isVisibleShowNewsCardForm"
      :newsId="showNewsItemId"
      @closeCardForm="onShowNewsItem"
    ></ShowNewsCardForm>

    <EditNewsCardForm
      v-if="isVisibleEditNewsCardForm"
      :newsId="editNewsItemId"
      @closeCardForm="() => onEditNewsFormVisible('')"
      @saveCardForm="onEditNewsItem"
    ></EditNewsCardForm>
  </div>
</template>
