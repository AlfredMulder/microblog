"""add language to posts

Revision ID: 99fe06aad7c6
Revises: 44eadb2d7e60
Create Date: 2019-02-28 11:06:24.024751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99fe06aad7c6'
down_revision = '44eadb2d7e60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
