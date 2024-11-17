from pydantic import BaseModel, ConfigDict
from datetime import datetime


class NewsBase(BaseModel):
    title: str
    text: str


class NewsRead(NewsBase):
    model_config = ConfigDict(from_attributes=True)
    
    uuid: str
    created_at: datetime
    updated_at: datetime


class NewsCreate(NewsBase):
    pass


class NewsUpdate(NewsCreate):
    pass
