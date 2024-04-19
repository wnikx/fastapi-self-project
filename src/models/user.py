from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.utils.custom_types import created_at, int_pk, str_256, updated_at


class User(Base):
    """Таблица с информацией о юзерах"""

    __tablename__ = "user"

    id: Mapped[int_pk]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    hashed_password: Mapped[str_256]
    email: Mapped[str_256] = mapped_column(unique=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id", ondelete="CASCADE"))
    position_id: Mapped[int] = mapped_column(ForeignKey("position.id", ondelete="CASCADE"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Company"] = relationship(back_populates="users")  # type: ignore  # noqa: PGH003
    position: Mapped["Position"] = relationship(back_populates="users")  # type: ignore  # noqa: PGH003
    role: Mapped["Role"] = relationship(back_populates="users")  # type: ignore  # noqa: PGH003
