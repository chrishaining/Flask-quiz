"""empty message

Revision ID: 0ebdb1fa05c1
Revises: a7f105581861
Create Date: 2020-02-24 15:10:24.664159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ebdb1fa05c1'
down_revision = 'a7f105581861'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('multiple_choice_topic', 'fifth')
    op.drop_column('multiple_choice_topic', 'dunno')
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
    op.add_column('multiple_choice_topic', sa.Column('dunno', sa.VARCHAR(length=64), nullable=True))
    op.add_column('multiple_choice_topic', sa.Column('fifth', sa.VARCHAR(length=64), nullable=True))
    # ### end Alembic commands ###