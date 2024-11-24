from sqlalchemy import delete, text
from sqlalchemy.engine import Result
from uuid import uuid4
from src.news.models import News
from src.news.schemas import NewsRead, NewsCreate, NewsUpdate
from src.tags.schemas import TagsRead
from src.service import Service


class NewsService(Service):
    def get_news(self, uuid_tag) -> list[NewsRead]:
        if uuid_tag == 'all':
            stmt = text(
                """
                    SELECT title, text, uuid, created_at, updated_at, tags.uuid, tags.name, tags_uuid FROM news_house.news 
                    JOIN news_house.tags ON news.tags_uuid = tags.uuid;
                """
            )
        else:
            stmt = text(
                f"""
                    SELECT title, text, uuid, created_at, updated_at, tags.uuid, tags.name, tags_uuid FROM news_house.news 
                    JOIN news_house.tags ON news.tags_uuid = tags.uuid
                    WHERE news.tags_uuid = '{uuid_tag}';
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
        return news_list

    def get_news_by_id(self, uuid: str) -> NewsRead:
        stmt = text(
            f"""
            SELECT title, text, uuid, created_at, updated_at, tags.uuid, tags.name FROM news_house.news 
            JOIN news_house.tags ON news.tags_uuid = tags.uuid
            WHERE news.uuid = '{uuid}'
            """
            )
        result: Result = self.session.execute(stmt)
        res = result.fetchone()
        news = NewsRead(
            title=res[0],
            text=res[1],
            uuid=res[2],
            created_at=res[3],
            updated_at=res[4],
            tags=TagsRead(
                name=res[6],
                uuid=res[5]
            )
        )
        return news

    def create_news(self, news: NewsCreate) -> NewsRead:
        add_news = News(**news.model_dump(), uuid=str(uuid4()))
        self.session.add(add_news)
        self.session.commit()
        new_news = self.get_news_by_id(add_news.uuid)
        return new_news

    def update_news(self, news: NewsRead, news_update: NewsUpdate) -> NewsRead:
        news_update = news_update.model_dump()
        for key, value in news_update.items():
            if value != None:
                setattr(news, key, value)
        self.session.commit()
        self.session.refresh(news)
        self.session.expire_all()
        new_news = self.get_news_by_id(news.uuid)
        return new_news

    def delete_news(self, uuid: str) -> None:
        try:
            stmt = delete(News).filter(News.uuid == uuid)
            self.session.execute(stmt)
            self.session.commit()
            return 'success'
        except Exception as ex:
            self.session.rollback()
            return f'excption {ex}'
