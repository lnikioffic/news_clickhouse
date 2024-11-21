from sqlalchemy.orm import Session
from src.database import db
from fastapi import Depends
from typing import Annotated


class Service:
    def __init__(self, session: Annotated[Session, Depends(db.get_session)]) -> None:
        self.session = session
