from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from src.tags.schemas import TagsRead


class NewsBase(BaseModel):
    title: str = Field(min_length=6, max_length=100)
    text: str = Field(min_length=20)


class NewsRead(NewsBase):
    model_config = ConfigDict(from_attributes=True)

    uuid: str
    tags: TagsRead
    created_at: datetime
    updated_at: datetime


class NewsCreate(NewsBase):
    tags_uuid: str


class NewsUpdate(NewsCreate):
    pass