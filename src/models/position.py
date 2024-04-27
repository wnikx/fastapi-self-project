from sqlalchemy import Column, Index, Integer, Sequence, String, func
from sqlalchemy.orm import Mapped, foreign, relationship, remote
from sqlalchemy_utils import Ltree, LtreeType

from src.database.database import async_engine
from src.models.base import Base
from src.utils.custom_types import int_pk, str_256

id_seq = Sequence("position_id_seq")


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

    def __init__(self, _position_title, parent=None):
        _id = async_engine.execute(id_seq)
        self.id = _id
        self.position_title = _position_title
        ltree_id = Ltree(str(_id))
        self.path = ltree_id if parent is None else parent.path + ltree_id

    __table_args__ = (Index("ix_nodes_path", path, postgresql_using="gist"),)
