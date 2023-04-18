"""account confirmation

Revision ID: 618f76668752
Revises: 63af27cca29f
Create Date: 2023-03-09 11:03:18.759663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '618f76668752'
down_revision = '63af27cca29f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###
