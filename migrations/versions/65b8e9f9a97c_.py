"""empty message

Revision ID: 65b8e9f9a97c
Revises: b2cdd6cb0fb9
Create Date: 2020-02-24 14:04:03.959207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65b8e9f9a97c'
down_revision = 'b2cdd6cb0fb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('topic', 'user_answer',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.drop_column('topic', 'suggested_answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('suggested_answer', sa.VARCHAR(length=64), nullable=True))
    op.alter_column('topic', 'user_answer',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###
