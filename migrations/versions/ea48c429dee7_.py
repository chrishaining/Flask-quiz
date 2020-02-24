"""empty message

Revision ID: ea48c429dee7
Revises: 861bc4a69e25
Create Date: 2020-02-24 12:19:45.720212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea48c429dee7'
down_revision = '861bc4a69e25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('answer', sa.String(length=64), nullable=True))
    op.alter_column('topic', 'user_answer',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('topic', 'user_answer',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_column('topic', 'answer')
    # ### end Alembic commands ###