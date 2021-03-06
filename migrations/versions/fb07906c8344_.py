"""empty message

Revision ID: fb07906c8344
Revises: 
Create Date: 2021-01-22 20:39:47.553852

"""
from alembic import op
import sqlalchemy as sa


from models.utilities import UUID2STR, UTCDatetime

# revision identifiers, used by Alembic.
revision = 'fb07906c8344'
down_revision = None
branch_labels = ("schema")
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gateway',
    sa.Column('uuid', UUID2STR(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created', UTCDatetime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('bearer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('smart_meter',
    sa.Column('uuid', UUID2STR(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created', UTCDatetime(), nullable=True),
    sa.Column('voltage', sa.Float(), nullable=True, comment='V'),
    sa.Column('current', sa.Float(), nullable=True, comment='A'),
    sa.Column('power', sa.Float(), nullable=True, comment='W'),
    sa.Column('total_current', sa.Float(), nullable=True, comment='kWh'),
    sa.Column('sensor', sa.String(), nullable=False, comment='sensor name'),
    sa.Column('gateway', sa.String(), nullable=False, comment='gateway name'),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('smart_meter')
    op.drop_table('gateway')
    # ### end Alembic commands ###
