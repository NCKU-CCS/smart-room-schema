"""empty message

Revision ID: d0e1882002f4
Revises: f9325c07f2a4
Create Date: 2021-04-21 16:20:55.455550

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd0e1882002f4'
down_revision = 'f9325c07f2a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device', sa.Column('room', sa.String(), nullable=True))
    op.execute('UPDATE device SET room=608')
    op.alter_column('device', 'room', nullable=False)
    op.drop_constraint('device_name_location_key', 'device', type_='unique')
    op.create_unique_constraint(None, 'device', ['name', 'location', 'room'])
    op.add_column('sensor', sa.Column('room', sa.String(), nullable=True))
    op.execute('UPDATE sensor SET room=608')
    op.alter_column('sensor', 'room', nullable=False)
    op.drop_constraint('sensor_name_location_key', 'sensor', type_='unique')
    op.create_unique_constraint(None, 'sensor', ['name', 'location', 'room'])
    op.alter_column('sensor_data', 'temperature',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               comment='celsius',
               existing_comment='C',
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sensor_data', 'temperature',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               comment='C',
               existing_comment='celsius',
               existing_nullable=True)
    op.drop_constraint(None, 'sensor', type_='unique')
    op.create_unique_constraint('sensor_name_location_key', 'sensor', ['name', 'location'])
    op.drop_column('sensor', 'room')
    op.drop_constraint(None, 'device', type_='unique')
    op.create_unique_constraint('device_name_location_key', 'device', ['name', 'location'])
    op.drop_column('device', 'room')
    # ### end Alembic commands ###
