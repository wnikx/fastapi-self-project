from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.custom_types import created_at, int_pk, str_256, updated_at
from src.models import Base
from src.registration.schema import SignUpSchema


class Account(Base):
    """Таблица с информацией о компаниях"""

    __tablename__ = "account"

    id: Mapped[int_pk]
    account_name: Mapped[str_256] = None
    created: Mapped[created_at]


class Invite(Base):
    """Таблица со связью инвайта и аккаунта"""

    __tablename__ = "invite"

    id: Mapped[int_pk]
    account: Mapped[str_256]
    invite_token: Mapped[str_256]


class User(Base):
    """Таблица с информацией о юзерах"""

    __tablename__ = "user"

    id: Mapped[int_pk]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    password: Mapped[str_256]
    account: Mapped[str_256]


class Company(Base):
    """Таблица с информацией о компаниях"""

    __tablename__ = "company"

    id: Mapped[int_pk]
    company_name: Mapped[str_256]


class Position(Base):
    """Таблица с информацией о должностях"""

    __tablename__ = "position"

    id: Mapped[int_pk]
    position_title: Mapped[str_256]


class UserAccount(Base):
    """Таблица для хранения информации о связях user-account"""

    __tablename__ = "user_account"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )
    account_id: Mapped[int] = mapped_column(
        ForeignKey("account.id", ondelete="CASCADE"),
        primary_key=True,
    )


class UserCompany(Base):
    """Таблица для хранения связей между пользователями и компаниями"""

    __tablename__ = "user_company"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id", ondelete="CASCADE"),
        primary_key=True,
    )


class UserPosition(Base):
    """Таблица для хранения информации связях пользователей и их должностях"""

    __tablename__ = "user_position"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )
    position_id: Mapped[int] = mapped_column(
        ForeignKey("position.id", ondelete="CASCADE"),
        primary_key=True,
    )
