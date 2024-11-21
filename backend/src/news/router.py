from fastapi import APIRouter, Depends
from typing import Annotated
from src.news.schemas import NewsRead, NewsCreate, NewsUpdate
from src.news.dependencies import get_newses, valid_news_id
from src.news.service import NewsService

router = APIRouter(prefix='/news', tags=['news'])


@router.get('/', response_model=list[NewsRead])
def get_news(newses: Annotated[list[NewsRead], Depends(get_newses)]):
    return newses


@router.post('/', response_model=NewsRead)
def create_news(news: NewsCreate, service: Annotated[NewsService, Depends()]):
    new_news = service.create_news(news)
    return new_news


@router.get('/{news_id}', response_model=NewsRead)
def get_news_by_id(news: Annotated[NewsRead, Depends(valid_news_id)]):
    return news


@router.put('/{news_id}', response_model=NewsRead)
def update_news(
    news_update: NewsUpdate,
    news: Annotated[NewsRead, Depends(valid_news_id)],
    service: Annotated[NewsService, Depends()],
):
    news_updated = service.update_news(news, news_update)
    return news_updated


@router.delete('/{news_id}')
def delete_news(
    news: Annotated[NewsRead, Depends(valid_news_id)],
    service: Annotated[NewsService, Depends()],
):
    me = service.delete_news(news.uuid)
    return {'message': me}
