from sqlalchemy.orm import Mapped, relationship

from src.models.base import Base
from src.utils.custom_types import created_at, int_pk, str_256, updated_at


class Company(Base):
    """Таблица с информацией о компаниях"""

    __tablename__ = "company"

    id: Mapped[int_pk]
    company_name: Mapped[str_256]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    users: Mapped[list["User"]] = relationship(back_populates="company")  # type: ignore  # noqa: PGH003
