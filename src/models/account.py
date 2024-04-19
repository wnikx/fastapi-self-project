from sqlalchemy.orm import Mapped

from src.models.base import Base
from src.utils.custom_types import created_at, int_pk, str_256


class Account(Base):
    """Таблица с информацией о зарегестрированных e-mail'ах"""

    __tablename__ = "account"

    id: Mapped[int_pk]
    email: Mapped[str_256]
    created: Mapped[created_at]
