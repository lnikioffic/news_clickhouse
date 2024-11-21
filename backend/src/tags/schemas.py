from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class TagsBase(BaseModel):
    name: str


class TagsRead(TagsBase):
    model_config = ConfigDict(from_attributes=True)

    uuid: str


class TagsCreate(TagsBase):
    pass
