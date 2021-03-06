"""empty message

Revision ID: f0e87bd5280e
Revises: dae40a8037bc
Create Date: 2019-01-20 12:35:55.299597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0e87bd5280e'
down_revision = 'dae40a8037bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('maids', 'scheduled_to_meet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('maids', sa.Column('scheduled_to_meet', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
