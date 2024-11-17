from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class NewsBase(BaseModel):
    title: str = Field(min_length=6, max_length=100)
    text: str = Field(min_length=20)


class NewsRead(NewsBase):
    model_config = ConfigDict(from_attributes=True)
    
    uuid: str
    created_at: datetime
    updated_at: datetime


class NewsCreate(NewsBase):
    pass


class NewsUpdate(NewsCreate):
    pass
