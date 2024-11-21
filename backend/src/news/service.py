from sqlalchemy import delete, select, join, text
from sqlalchemy.engine import Result
from uuid import uuid4
from src.news.models import News
from src.tags.models import Tags
from src.news.schemas import NewsRead, NewsCreate, NewsUpdate
from src.tags.schemas import TagsRead
from src.service import Service


class NewsService(Service):
    def get_news(self) -> list[NewsRead]:
        # stmt = select(News).join(Tags, News.tags_uuid == Tags.uuid)
        stmt = text(
            """
                SELECT title, text, uuid, created_at, updated_at, tags.uuid, tags.name FROM news_house.news 
                JOIN news_house.tags ON news.tags_uuid = tags.uuid;
            """
        )
        result: Result = self.session.execute(stmt)
        news_list = []
        res = result.fetchall()
        for r in res:
            news_item = NewsRead(
                title=r[0],
                text=r[1],
                uuid=r[2],
                created_at=r[3],
                updated_at=r[4],
                tags=TagsRead(
                    name=r[6],
                    uuid=r[5]
                )
            )
            news_list.append(news_item)
        # for row in res:
        #     news_item = NewsRead(
        #         title=row[0],
        #         text=row[1],
        #         uuid=row[2],
        #         created_at=row[3],
        #         updated_at=row[4],
        #         tags=TagsRead(row[5], row[6]),  # Создаем список тегов
        #     )
        #     news_list.append(news_item)
        return news_list

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
