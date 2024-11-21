from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from clickhouse_sqlalchemy import engines
from src.database import DATABASE
from datetime import datetime
from src.models import Base


class News(Base):
    __tablename__ = 'news'
    __table_args__ = (
        engines.MergeTree(order_by=['uuid']),
        {'schema': DATABASE},
    )

    uuid: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]
    tags_uuid: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
