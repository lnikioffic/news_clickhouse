from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from src.news.schemas import NewsRead
from src.news.service import NewsService


error_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'User not found',
)


def valid_news_id(
    news_id: Annotated[str, Path], service: Annotated[NewsService, Depends()]
) -> NewsRead | None:
    news = service.get_news_by_id(news_id)

    if not news:
        raise error_found

    return news


def get_newses(service: Annotated[NewsService, Depends()]) -> list[NewsRead]:
    newses = service.get_news()
    return newses
