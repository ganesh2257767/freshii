"""empty message

Revision ID: 3495a5b93f1f
Revises: b085f25d575a
Create Date: 2024-08-24 01:13:23.130431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3495a5b93f1f'
down_revision = 'b085f25d575a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freshii_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('user')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freshii_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
