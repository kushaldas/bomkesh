"""empty message

Revision ID: e20a36754f8d
Revises: None
Create Date: 2020-08-28 18:00:38.009585

"""

# revision identifiers, used by Alembic.
revision = 'e20a36754f8d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dnsqueue',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('domain_name', sa.String(), nullable=False),
    sa.Column('domain_class', sa.String(), nullable=False),
    sa.Column('domain_type', sa.String(), nullable=False),
    sa.Column('ip_a', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rawpacket',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('source_ip', sa.String(), nullable=False),
    sa.Column('destination_ip', sa.String(), nullable=False),
    sa.Column('source_port', sa.Integer(), nullable=False),
    sa.Column('destination_port', sa.Integer(), nullable=False),
    sa.Column('packet_type', sa.Enum('TCP', 'UDP', name='packettypeenum'), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rawpacket')
    op.drop_table('dnsqueue')
    # ### end Alembic commands ###