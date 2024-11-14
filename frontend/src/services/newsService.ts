import type News from "@/models/News";

export function getNews(): Array<News> {
    const arr: Array<News> = []

    for (let i = 0; i < 20; i++)
        arr.push({
            id: `${i}`,
            title: `Title № ${i + 1}`,
            text: '13',
            author: 'Ivan',
            date: '10.11.2024'
        })

    return arr
}
// Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Donec rutrum congue leo eget malesuada.
export function updateNews(news: News) {

}

export function remoeNews(news: News) {

}

export function createNews(news: News): News {
    return { ...news, id: '130', date: '13.13.2024' }
}