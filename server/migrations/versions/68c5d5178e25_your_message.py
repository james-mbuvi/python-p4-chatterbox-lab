"""your message

Revision ID: 68c5d5178e25
Revises: 
Create Date: 2024-04-06 00:28:42.859119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68c5d5178e25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
