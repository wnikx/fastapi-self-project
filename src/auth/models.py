import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base

created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    ),
]


class Account(Base):
    """Таблица с информацией о компаниях"""

    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_name: Mapped[str]
    created: Mapped[created_at]


class Invite(Base):
    """Таблица со связью инвайта и аккаунта"""

    __tablename__ = "invites"

    id: Mapped[int] = mapped_column(primary_key=True)
