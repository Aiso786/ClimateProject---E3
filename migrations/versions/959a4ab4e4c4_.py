"""empty message

Revision ID: 959a4ab4e4c4
Revises: 717e19921630
Create Date: 2022-02-09 18:03:24.858618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959a4ab4e4c4'
down_revision = '717e19921630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('img', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'img', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'img', type_='foreignkey')
    op.drop_column('img', 'user_id')
    # ### end Alembic commands ###
