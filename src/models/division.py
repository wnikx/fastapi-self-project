from tokenize import String

from sqlalchemy import Column, Index, Integer, Sequence, func
from sqlalchemy.orm import Mapped, foreign, relationship, remote
from sqlalchemy_utils import Ltree, LtreeType

from src.models import Base
from src.utils.custom_types import str_256

id_seq = Sequence("position_id_seq")


class StructAdmPositions(Base):
    """A class representing administrative positions in a hierarchical structure.

    This class maps to the 'struct_adm_positions' table in the database, storing administrative positions
    along with their hierarchical relationships.

    Parameters
    ----------
    id : int
        The unique identifier for the administrative position.
    note : str
        A description or note associated with the administrative position.
    parent : StructAdmPositions, optional
        The parent administrative position. Default is None.

    Attributes
    ----------
    id : int
        The unique identifier for the administrative position.
    note : str
        A description or note associated with the administrative position.
    path : LtreeType
        The path of the administrative position in the hierarchical structure.
    parent : StructAdmPositions
    The parent administrative position.

    """

    __tablename__ = "struct_adm_positions"

    id = Column(Integer, id_seq, primary_key=True)
    note: Mapped[str_256]
    path = Column(LtreeType, nullable=False)

    parent = relationship(
        "Position",
        primaryjoin=(remote(path) == foreign(foreign(func.subpath(path, 0, -1)))),
        backref="children",
        viewonly=True,
    )

    def __init__(self, id: int, note, parent=None):
        self.id = id
        self.note = note
        ltree_id = Ltree(str(id))
        self.path = ltree_id if parent is None else parent.path + ltree_id

    __table_args__ = (Index("ix_nodes_path", path, postgresql_using="gist"),)
