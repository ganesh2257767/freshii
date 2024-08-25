"""empty message

Revision ID: 052e0a6ff4b8
Revises: 3495a5b93f1f
Create Date: 2024-08-25 13:26:50.883907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '052e0a6ff4b8'
down_revision = '3495a5b93f1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freshii_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('entered_by_user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('updated_by_user_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('freshii_data_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['updated_by_user_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['entered_by_user_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freshii_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('freshii_data_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.drop_column('updated_by_user_id')
        batch_op.drop_column('entered_by_user_id')

    # ### end Alembic commands ###
