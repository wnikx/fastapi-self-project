from typing import Any

from sqlalchemy import Column, Index, Integer, Sequence, func
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, foreign, relationship, remote
from sqlalchemy_utils import Ltree, LtreeType

from src.config import settings
from src.models.base import Base
from src.utils.custom_types import str_256

id_seq = Sequence("position_id_seq")

async_engine = create_async_engine(settings.DB_URL, echo=False)
async_session_maker = async_sessionmaker(bind=async_engine)


class Position(Base):
    """Таблица с информацией о должностях"""

    __tablename__ = "position"

    id = Column(Integer, id_seq, primary_key=True)
    position_title: Mapped[str_256]
    path = Column(LtreeType, nullable=False)

    parent = relationship(
        "Position",
        primaryjoin=(remote(path) == foreign(foreign(func.subpath(path, 0, -1)))),
        backref="children",
        viewonly=True,
    )
    users: Mapped[list["User"]] = relationship(back_populates="position")  # type: ignore  # noqa: PGH003

    def __init__(self, id: int, position_title, parent=None):
        self.id = id
        self.position_title = position_title
        ltree_id = Ltree(str(id))
        self.path = ltree_id if parent is None else parent.path + ltree_id

    __table_args__ = (Index("ix_nodes_path", path, postgresql_using="gist"),)
