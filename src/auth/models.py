from sqlalchemy.orm import Mapped, mapped_column

from src.custom_types import created_at, int_pk, updated_at
from src.models import Base


class Account(Base):
    """Таблица с информацией о компаниях"""

    __tablename__ = "accounts"

    id: Mapped[int_pk]
    account_name: Mapped[str]
    created: Mapped[created_at]


class Invite(Base):
    """Таблица со связью инвайта и аккаунта"""

    __tablename__ = "invites"

    id: Mapped[int_pk]
    account_name: Mapped[str]
    invite_token: Mapped[str]
