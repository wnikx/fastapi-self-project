import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.custom_types import created_at, int_pk, str_256, updated_at
from src.models import Base
from src.registration.schema import SignUpSchema


class Account(Base):
    """Таблица с информацией о зарегестрированных e-mail'ах"""

    __tablename__ = "account"

    id: Mapped[int_pk]
    email: Mapped[str_256]
    created: Mapped[created_at]


class Invite(Base):
    """Таблица со связью инвайта и аккаунта"""

    __tablename__ = "invite"

    id: Mapped[int_pk]
    email: Mapped[str_256]
    invite_token: Mapped[str_256]


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

    company: Mapped["Company"] = relationship(back_populates="users")
    position: Mapped["Position"] = relationship(back_populates="users")
    role: Mapped["Role"] = relationship(back_populates="users")


class Company(Base):
    """Таблица с информацией о компаниях"""

    __tablename__ = "company"

    id: Mapped[int_pk]
    company_name: Mapped[str_256]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    users: Mapped[list["User"]] = relationship(back_populates="company")


class Position(Base):
    """Таблица с информацией о должностях"""

    __tablename__ = "position"

    id: Mapped[int_pk]
    position_title: Mapped[str_256]

    users: Mapped[list["User"]] = relationship(back_populates="position")


class RoleName(enum.Enum):
    admin = "admin"
    user = "user"
    guest = "guest"


class Role(Base):
    """Таблица с информацией о роли"""

    __tablename__ = "role"

    id: Mapped[int_pk]
    role: Mapped[RoleName]

    users: Mapped[list["User"]] = relationship(back_populates="role")


# class UserAccount(Base):
#     """Таблица для хранения информации о связях user-account"""

#     __tablename__ = "user_account"

#     user_id: Mapped[int] = mapped_column(
#         ForeignKey("user.id", ondelete="CASCADE"),
#         primary_key=True,
#     )
#     account_id: Mapped[int] = mapped_column(
#         ForeignKey("account.id", ondelete="CASCADE"),
#         primary_key=True,
#     )


# class UserCompany(Base):
#     """Таблица для хранения связей между пользователями и компаниями"""

#     __tablename__ = "user_company"

#     user_id: Mapped[int] = mapped_column(
#         ForeignKey("user.id", ondelete="CASCADE"),
#         primary_key=True,
#     )
#     company_id: Mapped[int] = mapped_column(
#         ForeignKey("company.id", ondelete="CASCADE"),
#         primary_key=True,
#     )


# class UserPosition(Base):
#     """Таблица для хранения информации связях пользователей и их должностях"""

#     __tablename__ = "user_position"

#     user_id: Mapped[int] = mapped_column(
#         ForeignKey("user.id", ondelete="CASCADE"),
#         primary_key=True,
#     )
#     position_id: Mapped[int] = mapped_column(
#         ForeignKey("position.id", ondelete="CASCADE"),
#         primary_key=True,
#     )
