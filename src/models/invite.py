from sqlalchemy.orm import Mapped

from src.models.base import Base
from src.utils.custom_types import int_pk, str_256


class Invite(Base):
    """Таблица со связью инвайта и аккаунта"""

    __tablename__ = "invite"

    id: Mapped[int_pk]
    email: Mapped[str_256]
    invite_token: Mapped[str_256]
