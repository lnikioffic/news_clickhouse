from sqlalchemy import delete, select
from sqlalchemy.engine import Result
from uuid import uuid4
from src.tags.models import Tags
from src.tags.schemas import TagsCreate, TagsRead
from src.service import Service


class TagsService(Service):
    def get_tegs(self) -> list[TagsRead]:
        stmt = select(Tags)
        result: Result = self.session.execute(stmt)
        tags = result.scalars().all()
        return list(tags)

    def create_tags(self, news: TagsCreate) -> TagsRead:
        add_tags = Tags(**news.model_dump(), uuid=str(uuid4()))
        self.session.add(add_tags)
        self.session.commit()
        return add_tags
