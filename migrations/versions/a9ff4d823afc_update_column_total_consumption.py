"""Update Column: total_consumption

Revision ID: a9ff4d823afc
Revises: d0e1882002f4
Create Date: 2021-08-10 23:13:20.132744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from models.utilities import UUID2STR, UTCDatetime

# revision identifiers, used by Alembic.
revision = 'a9ff4d823afc'
down_revision = 'd0e1882002f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('meter_data', 'total_current', nullable=False, new_column_name='total_consumption')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('meter_data', 'total_consumption', nullable=False, new_column_name='total_current')
    # ### end Alembic commands ###