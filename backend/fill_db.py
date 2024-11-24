from sqlalchemy import Result, func, select
from sqlalchemy.orm import Session
from uuid import uuid4
from mimesis import Generic
from mimesis.locales import Locale
import random

from src.database import db
from src.tags.schemas import TagsRead, TagsCreate
from src.tags.models import Tags
from src.news.schemas import NewsRead, NewsCreate
from src.news.models import News


tags_news = ['Образование', 'Гороскоп', 'Политика', 'Игры', 'IT']


def get_tags(session: Session) -> list[TagsRead]:
    stmt = select(Tags)
    result: Result = session.execute(stmt)
    tags = result.scalars().all()
    return list(tags)


def create_tags(tags: list[TagsCreate], session: Session):
    add_tags = [Tags(**tag.model_dump(), uuid=str(uuid4())) for tag in tags]
    session.add_all(add_tags)
    session.commit()
    return get_tags(session)


def create_news(newses: list[NewsCreate], session: Session):
    add_newses = [News(**news.model_dump(), uuid=str(uuid4())) for news in newses]
    session.add_all(add_newses)
    session.commit()


def get_count_news(session: Session):
    stmt = select(func.count(News.uuid))
    result = session.execute(stmt)
    count = result.scalar()
    return count


def main():
    with db.session() as session:
        tags = get_tags(session)

        for tag in tags:
            if tag.name not in tags_news:
                print(f'{tag.name}')
            if tag.name in tags_news:
                tags_news.remove(tag.name)

        if len(tags_news) == 0:
            print('Все теги уже созданы')
        else:
            t_name = [TagsCreate(name=name) for name in tags_news]
            tags = create_tags(t_name, session)

        uuid_tags = [tag.uuid for tag in tags]

        count_news = get_count_news(session)
        if count_news >= 100:
            print(f'количество новостей {count_news}')
            return

        generic = Generic(locale=Locale.RU)
        news_list = []
        for _ in range(100):
            news_item = NewsCreate(
                title=generic.text.title(),  # Заголовок
                text=generic.text.text(5),  # Текст от 20 до 200 символов
                tags_uuid=random.choice(uuid_tags),  # Генерация UUID для тегов
            )
            news_list.append(news_item)

        create_news(news_list, session)


if __name__ == '__main__':
    main()
