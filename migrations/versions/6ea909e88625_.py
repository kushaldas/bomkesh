"""empty message

Revision ID: 6ea909e88625
Revises: 31cc014da672
Create Date: 2019-09-26 01:50:59.719014

"""

# revision identifiers, used by Alembic.
revision = '6ea909e88625'
down_revision = '31cc014da672'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dnsqueue', sa.Column('ip', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dnsqueue', 'ip')
    # ### end Alembic commands ###