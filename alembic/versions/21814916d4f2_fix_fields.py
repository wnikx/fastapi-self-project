"""fix fields

Revision ID: 21814916d4f2
Revises: 63d498dd10ab
Create Date: 2024-04-17 18:42:06.820830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21814916d4f2'
down_revision: Union[str, None] = '63d498dd10ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('account', sa.String(length=256), nullable=False))
    op.drop_column('account', 'account_name')
    op.add_column('invite', sa.Column('account', sa.String(length=256), nullable=False))
    op.drop_column('invite', 'account_name')
    op.add_column('user', sa.Column('password', sa.String(length=256), nullable=False))
    op.add_column('user', sa.Column('account', sa.String(length=256), nullable=False))
    op.drop_column('user_account', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_account', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('user', 'account')
    op.drop_column('user', 'password')
    op.add_column('invite', sa.Column('account_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.drop_column('invite', 'account')
    op.add_column('account', sa.Column('account_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.drop_column('account', 'account')
    # ### end Alembic commands ###
