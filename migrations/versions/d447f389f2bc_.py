"""empty message

Revision ID: d447f389f2bc
Revises: 96fcae0b87d0
Create Date: 2024-08-23 19:53:53.669421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd447f389f2bc'
down_revision = '96fcae0b87d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freshii_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=False))
        batch_op.create_unique_constraint(None, ['date'])
        batch_op.drop_column('data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freshii_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', sa.DATE(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('date')

    # ### end Alembic commands ###
