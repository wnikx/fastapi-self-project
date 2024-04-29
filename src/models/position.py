from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base
from src.utils.custom_types import int_pk, str_256


class Position(Base):
    """Таблица с информацией о должностях"""

    __tablename__ = "position"

    id: Mapped[int_pk]
    position_title: Mapped[str_256]

    users: Mapped[list["User"]] = relationship(back_populates="position")  # type: ignore  # noqa: PGH003
