"""alter column name

Revision ID: 3bc95b843349
Revises: 
Create Date: 2021-02-22 05:48:02.887625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bc95b843349'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'students',
        'st_id',
        new_column_name='student_id'
    )


def downgrade():
    op.alter_column(
        'students',
        'student_id',
        new_column_name='st_id'
    )


