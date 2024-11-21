from sqlalchemy.orm import Mapped, mapped_column, relationship
from clickhouse_sqlalchemy import engines
from src.database import DATABASE
from src.models import Base


class Tags(Base):
    __tablename__ = 'tags'
    __table_args__ = (
        engines.MergeTree(order_by=['uuid']),
        {'schema': DATABASE},
    )
    uuid: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
