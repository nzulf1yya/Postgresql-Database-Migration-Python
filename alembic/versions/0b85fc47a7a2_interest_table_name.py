"""interest table name

Revision ID: 0b85fc47a7a2
Revises: dfea060dfde4
Create Date: 2021-02-22 10:18:17.313667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b85fc47a7a2'
down_revision = 'dfea060dfde4'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'interests',
        'interest',
        new_column_name='interests'
    )


def downgrade():
    op.alter_column(
        'interests',
        'interests',
        new_column_name='interest'
    )