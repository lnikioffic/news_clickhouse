<script lang="ts" setup>
// vue
import { ref, onMounted, type Ref } from 'vue'
// components
import Header from './components/TheHeader.vue'
import NewsCard from '@/components/NewsCard.vue'
import CreateNewsCardForm from './components/CreateNewsCardForm.vue'
import ShowNewsCardForm from '@/components/ShowNewsCardForm.vue'
import EditNewsCardForm from '@/components/EditNewsCardForm.vue'
import CreateTagForm from './components/CreateTagForm.vue'
//services
import { getNews, createNews, remoeNews, updateNews } from '@/services/newsService'
import { createTag, getTags } from '@/services/tagsService'
// types
import type News from '@/models/News'
import type NewsBase from './models/NewsBase'
import type TagBase from './models/TagBase'
import type Tag from './models/Tag'

// refs
const currentFilter = ref('all')
const newsArr: Ref<Array<News>> = ref([])
const tags: Ref<Array<Tag>> = ref([])

onMounted(async () => {
  newsArr.value = await getNews(currentFilter.value)
  tags.value = await getTags()
})

// filter
const onChangeFilter = async () => {
  newsArr.value = await getNews(currentFilter.value)
}

// create tag form
const isVisibleCreateTagCardForm: Ref<boolean> = ref(false)

const onCreateTagFormVisible = () => {
  isVisibleCreateTagCardForm.value = !isVisibleCreateTagCardForm.value
}

const onCreateTagItem = async (tagItem: TagBase) => {
  const newTag = await createTag(tagItem)
  tags.value.push(newTag)
  onCreateTagFormVisible()
}

//create news form
const isVisibleCreateNewsCardForm: Ref<boolean> = ref(false)

const onCreateNewsFormVisible = () => {
  isVisibleCreateNewsCardForm.value = !isVisibleCreateNewsCardForm.value
}

const onCreateNewsItem = async (newsItem: NewsBase) => {
  const newNews: News = await createNews(newsItem)
  if (currentFilter.value === 'all' || newNews.tags.uuid === currentFilter.value)
    newsArr.value.push(newNews)
  onCreateNewsFormVisible()
}

//show news form
const isVisibleShowNewsCardForm: Ref<boolean> = ref(false)
const showNewsItemId: Ref<string> = ref('')

const onShowNewsItem = (newsItemId: string) => {
  showNewsItemId.value = newsItemId
  isVisibleShowNewsCardForm.value = !isVisibleShowNewsCardForm.value
}

// remove news
const onRemoveNewsItem = async (id: string) => {
  await remoeNews(id)
  const newsIdx = newsArr.value.findIndex((x) => x.uuid === id)
  newsArr.value.splice(newsIdx, 1)
}

// edit news form
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
  <Header @createNews="onCreateNewsFormVisible" @createTag="onCreateTagFormVisible"></Header>

  <div class="container mt-16">
    <div>
      <div class="flex justify-between items-center">
        <h1 class="font-bold text-4xl select-none">#ОСНОВНЫЕ НОВОСТИ</h1>

        <div class="flex gap-x-3 items-center">
          <p class="font-bold text-lg">Категория:</p>
          <select
            class="border py-1 px-2 rounded-md outline-none hover:border-black"
            v-model="currentFilter"
            @change="onChangeFilter"
          >
            <option value="all" selected>Все</option>
            <option :value="tag.uuid" v-for="tag in tags">{{ tag.name }}</option>
          </select>
        </div>
      </div>

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

    <CreateTagForm
      v-if="isVisibleCreateTagCardForm"
      @closeCardForm="onCreateTagFormVisible"
      @saveCardForm="onCreateTagItem"
    ></CreateTagForm>
  </div>
</template>
