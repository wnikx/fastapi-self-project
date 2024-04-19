from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base
from src.utils.custom_types import int_pk
from src.utils.enums import RoleName


class Role(Base):
    """Таблица с информацией о роли"""

    __tablename__ = "role"

    id: Mapped[int_pk]
    role: Mapped[RoleName]

    users: Mapped[list["User"]] = relationship(back_populates="role")  # noqa: F821
