from fastapi import APIRouter, Depends
from typing import Annotated
from src.tags.service import TagsService
from src.tags.schemas import TagsRead, TagsCreate

router = APIRouter(prefix='/tags', tags=['tags'])


@router.get('/', response_model=list[TagsRead])
def get_news(service: Annotated[TagsService, Depends()]):
    tags = service.get_tegs()
    return tags


@router.post('/', response_model=TagsRead)
def create_news(tags: TagsCreate, service: Annotated[TagsService, Depends()]):
    new_tags = service.create_tags(tags)
    return new_tags
