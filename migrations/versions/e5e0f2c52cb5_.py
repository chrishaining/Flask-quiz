"""empty message

Revision ID: e5e0f2c52cb5
Revises: 37067ff7e5cc
Create Date: 2020-02-24 14:09:51.190658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5e0f2c52cb5'
down_revision = '37067ff7e5cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('multiple_choice_topic', sa.Column('option_d', sa.String(length=64), nullable=True))
    op.drop_column('multiple_choice_topic', 'fifth')
    op.drop_column('multiple_choice_topic', 'dunno')
    op.drop_column('multiple_choice_topic', 'outcome')
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
    op.add_column('multiple_choice_topic', sa.Column('outcome', sa.BOOLEAN(), nullable=True))
    op.add_column('multiple_choice_topic', sa.Column('dunno', sa.VARCHAR(length=64), nullable=True))
    op.add_column('multiple_choice_topic', sa.Column('fifth', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('multiple_choice_topic', 'option_d')
    # ### end Alembic commands ###
