"""empty message

Revision ID: 5182a6a2fe18
Revises: 03cfb25f6d91
Create Date: 2018-10-17 10:50:23.459016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5182a6a2fe18'
down_revision = '03cfb25f6d91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.Column('icon', sa.String(length=80), nullable=True),
    sa.Column('isactive', sa.Integer(), nullable=True),
    sa.Column('token', sa.String(length=256), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
