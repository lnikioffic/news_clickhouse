import axios from 'axios';

//models
import type News from '@/models/News';
import type NewsBase from '@/models/NewsBase';

const SERVER_URL = '/api/news'

export async function getNews(): Promise<Array<News>> {
    const { data } = await axios.get(SERVER_URL)
    return data
}

export async function getNewsById(id: string): Promise<News> {
    const { data } = await axios(`${SERVER_URL}/${id}`)
    return data
}

export async function createNews(news: NewsBase): Promise<News> {
    const { data } = await axios.post(SERVER_URL, news)
    return data
}

export async function remoeNews(id: string): Promise<void> {
    await axios.delete(`${SERVER_URL}/${id}`)
}

export async function updateNews(news: News): Promise<News> {
    const { data } = await axios.put(`${SERVER_URL}/${news.uuid}`, news)
    return data
}