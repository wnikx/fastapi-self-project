"""delete Position model fields

Revision ID: e5af2d968842
Revises: d4158296591c
Create Date: 2024-04-29 11:53:25.198892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e5af2d968842'
down_revision: Union[str, None] = 'd4158296591c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('account', 'email',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('account', 'created',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('company', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('company_id_seq'::regclass)"))
    op.alter_column('company', 'company_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('company', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('company', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('invite', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('invite', 'email',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('invite', 'invite_token',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('observer_task', 'user_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('observer_task', 'task_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('performer_task', 'user_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('performer_task', 'task_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('position', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('position', 'position_title',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.drop_index('ix_nodes_path', table_name='position', postgresql_using='gist')
    op.drop_column('position', 'path')
    op.alter_column('role', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('role', 'role',
               existing_type=postgresql.ENUM('admin', 'user', 'guest', name='rolename'),
               type_=sa.Enum('admin', 'user', 'guest', name='rolename'),
               existing_nullable=False)
    op.alter_column('task', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('task', 'title',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('task', 'author_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('task', 'assignee_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('task', 'deadline',
               existing_type=sa.DATE(),
               type_=sa.Date(),
               existing_nullable=False)
    op.alter_column('task', 'status',
               existing_type=postgresql.ENUM('to_do', 'in_progress', 'done', 'closed', name='statustask'),
               type_=sa.Enum('to_do', 'in_progress', 'done', 'closed', name='statustask'),
               existing_nullable=False)
    op.alter_column('task', 'estimated_time',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('user', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('user_id_seq'::regclass)"))
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.String(length=256),
               existing_nullable=False)
    op.alter_column('user', 'company_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('user', 'position_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('user', 'role_id',
               existing_type=sa.INTEGER(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('user', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('user', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'updated_at',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('user', 'created_at',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('user', 'role_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('user', 'position_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('user', 'company_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('user', 'last_name',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('user', 'first_name',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('user', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('user_id_seq'::regclass)"))
    op.alter_column('task', 'estimated_time',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('task', 'status',
               existing_type=sa.Enum('to_do', 'in_progress', 'done', 'closed', name='statustask'),
               type_=postgresql.ENUM('to_do', 'in_progress', 'done', 'closed', name='statustask'),
               existing_nullable=False)
    op.alter_column('task', 'deadline',
               existing_type=sa.Date(),
               type_=sa.DATE(),
               existing_nullable=False)
    op.alter_column('task', 'assignee_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('task', 'author_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('task', 'title',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('task', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('role', 'role',
               existing_type=sa.Enum('admin', 'user', 'guest', name='rolename'),
               type_=postgresql.ENUM('admin', 'user', 'guest', name='rolename'),
               existing_nullable=False)
    op.alter_column('role', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.add_column('position', sa.Column('path', sqlalchemy_utils.types.ltree.LtreeType(), autoincrement=False, nullable=False))
    op.create_index('ix_nodes_path', 'position', ['path'], unique=False, postgresql_using='gist')
    op.alter_column('position', 'position_title',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('position', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('performer_task', 'task_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('performer_task', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('observer_task', 'task_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('observer_task', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('invite', 'invite_token',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('invite', 'email',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('invite', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('company', 'updated_at',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('company', 'created_at',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('company', 'company_name',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('company', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('company_id_seq'::regclass)"))
    op.alter_column('account', 'created',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text("timezone('utc'::text, now())"))
    op.alter_column('account', 'email',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('account', 'id',
               existing_type=sa.Integer(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
