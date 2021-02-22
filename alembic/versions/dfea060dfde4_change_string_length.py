"""change string length

Revision ID: dfea060dfde4
Revises: 3bc95b843349
Create Date: 2021-02-22 08:55:57.422736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfea060dfde4'
down_revision = '3bc95b843349'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'st_name',
                    existing_type=sa.VARCHAR(length=15),
                    type_=sa.String(length=30),
                    existing_nullable=False)
    op.alter_column('students', 'st_last',
                    existing_type=sa.VARCHAR(length=15),
                    type_=sa.String(length=30),
                    existing_nullable=False)

def downgrade():
    op.alter_column('students', 'st_name',
                    existing_type=sa.VARCHAR(length=30),
                    type_=sa.String(length=15),
                    existing_nullable=False)
    op.alter_column('students', 'st_last',
                    existing_type=sa.VARCHAR(length=30),
                    type_=sa.String(length=15),
                    existing_nullable=False)
