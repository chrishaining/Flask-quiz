"""empty message

Revision ID: 9e668b26b256
Revises: 25caf7c282b4
Create Date: 2020-02-25 22:29:35.197473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e668b26b256'
down_revision = '25caf7c282b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('multiple_choice_topic', 'option_d')
    op.drop_column('multiple_choice_topic', 'fifth')
    op.drop_column('multiple_choice_topic', 'dunno')
    op.drop_column('topic', 'suggested_answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('suggested_answer', sa.VARCHAR(length=64), nullable=True))
    op.add_column('multiple_choice_topic', sa.Column('dunno', sa.VARCHAR(length=64), nullable=True))
    op.add_column('multiple_choice_topic', sa.Column('fifth', sa.VARCHAR(length=64), nullable=True))
    op.add_column('multiple_choice_topic', sa.Column('option_d', sa.VARCHAR(length=64), nullable=True))
    # ### end Alembic commands ###