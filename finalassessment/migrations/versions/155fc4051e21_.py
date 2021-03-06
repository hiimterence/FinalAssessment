"""empty message

Revision ID: 155fc4051e21
Revises: f0e87bd5280e
Create Date: 2019-01-20 12:37:03.467471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '155fc4051e21'
down_revision = 'f0e87bd5280e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('maids', sa.Column('scheduled_to_meet', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('maids', 'scheduled_to_meet')
    # ### end Alembic commands ###
