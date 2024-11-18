from fastapi import Depends
from typing import Annotated
from sqlalchemy import delete, select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from src.database import db
from uuid import uuid4
from src.models import News
from src.schemas import NewsRead, NewsCreate, NewsUpdate


class NewsService:
    def __init__(self, session: Annotated[Session, Depends(db.get_session)]) -> None:
        self.session = session

    def get_news(self) -> list[NewsRead]:
        stmt = select(News)
        result: Result = self.session.execute(stmt)
        news = result.scalars().all()
        return list(news)

    def get_news_by_id(self, uuid: str) -> NewsRead:
        news = self.session.get(News, uuid)
        return news

    def create_news(self, news: NewsCreate) -> NewsRead:
        add_news = News(**news.model_dump(), uuid=str(uuid4()))
        self.session.add(add_news)
        self.session.commit()
        return add_news

    def update_news(self, news: NewsRead, news_update: NewsUpdate) -> NewsRead:
        news_update = news_update.model_dump()
        for key, value in news_update.items():
            if value != None:
                setattr(news, key, value)
        self.session.commit()
        self.session.refresh(news)
        self.session.expire_all()
        return news

    def delete_news(self, uuid: str) -> None:
        try:
            stmt = delete(News).filter(News.uuid == uuid)
            self.session.execute(stmt)
            self.session.commit()
            return 'success'
        except Exception as ex:
            self.session.rollback()
            return f'excption {ex}'
