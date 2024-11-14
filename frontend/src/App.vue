<script lang="ts" setup>
// vue
import { ref, onMounted, type Ref } from 'vue'
// components
import Header from './components/TheHeader.vue'
import NewsCard from '@/components/NewsCard.vue'
import ShowNewsCardForm from '@/components/ShowNewsCardForm.vue'
import EditNewsCardForm from '@/components/EditNewsCardForm.vue'
//services
import { getNews, createNews } from '@/services/newsService'
// types
import type News from '@/models/News'

// refs
const newsArr: Ref<Array<News>> = ref([])

//show form
const isVisibleShowNewsCardForm: Ref<boolean> = ref(false)
const showNewsItem: Ref<News | null> = ref(null)

// edit form
const isVisibleEditNewsCardForm: Ref<boolean> = ref(false)
const editNewsItem: Ref<News | null> = ref(null)

onMounted(() => {
  newsArr.value = getNews()
})

const onRemoveNewsItem = (id: string) => {
  const deleteItem = newsArr.value.find((x) => x.id === id)
  if (!!deleteItem) {
    newsArr.value.splice(newsArr.value.indexOf(deleteItem), 1)
  }
}

const onShowNewsItem = (newsItem: News | null) => {
  showNewsItem.value = newsItem
  isVisibleShowNewsCardForm.value = !isVisibleShowNewsCardForm.value
}

const onEditNewsItem = (newsItem: News | null) => {
  editNewsItem.value = newsItem
  isVisibleEditNewsCardForm.value = !isVisibleEditNewsCardForm.value
}

const onSaveOrCreateNewsItem = (newsItem: News) => {
  const origItem = newsArr.value.find((x) => x.id === newsItem.id)
  if (!!origItem) {
    newsArr.value[newsArr.value.indexOf(origItem)] = newsItem
  } else {
    newsArr.value.push(createNews(newsItem))
  }
  onEditNewsItem(null)
}
</script>
<template>
  <Header @createNews="onEditNewsItem"></Header>

  <div class="container mt-16">
    <div>
      <h1 class="font-bold text-center text-4xl select-none">#ОСНОВНЫЕ НОВОСТИ</h1>

      <div class="mt-16 mb-20 grid grid-cols-3 gap-y-10 gap-x-14">
        <NewsCard
          v-for="newsItem in newsArr"
          :key="newsItem.id"
          :news="newsItem"
          @removeNews="onRemoveNewsItem"
          @showNews="onShowNewsItem"
          @editNews="onEditNewsItem"
        ></NewsCard>
      </div>
    </div>

    <ShowNewsCardForm
      v-if="isVisibleShowNewsCardForm"
      :news="showNewsItem"
      @closeCardForm="onShowNewsItem"
    ></ShowNewsCardForm>

    <EditNewsCardForm
      v-if="isVisibleEditNewsCardForm"
      :news="editNewsItem"
      @closeCardForm="onEditNewsItem"
      @saveCardForm="onSaveOrCreateNewsItem"
    ></EditNewsCardForm>
  </div>
</template>
