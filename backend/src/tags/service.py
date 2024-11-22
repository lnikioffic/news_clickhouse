from sqlalchemy import delete, select
from sqlalchemy.engine import Result
from uuid import uuid4
from src.tags.models import Tags
from src.tags.schemas import TagsCreate, TagsRead, TagsUpdate
from src.service import Service


class TagsService(Service):
    def get_tags(self) -> list[TagsRead]:
        stmt = select(Tags)
        result: Result = self.session.execute(stmt)
        tags = result.scalars().all()
        return list(tags)

    def get_tag_by_id(self, uuid: str) -> TagsRead:
        tag = self.session.get(Tags, uuid)
        return tag

    def create_tags(self, news: TagsCreate) -> TagsRead:
        add_tags = Tags(**news.model_dump(), uuid=str(uuid4()))
        self.session.add(add_tags)
        self.session.commit()
        return add_tags

    def update_news(self, tag: TagsRead, tag_update: TagsUpdate) -> TagsRead:
        tag_update = tag_update.model_dump()
        for key, value in tag_update.items():
            if value != None:
                setattr(tag, key, value)
        self.session.commit()
        self.session.refresh(tag)
        self.session.expire_all()
        return tag

    def delete_tag(self, uuid: str) -> None:
        try:
            stmt = delete(Tags).filter(Tags.uuid == uuid)
            self.session.execute(stmt)
            self.session.commit()
            return 'success'
        except Exception as ex:
            self.session.rollback()
            return f'excption {ex}'
