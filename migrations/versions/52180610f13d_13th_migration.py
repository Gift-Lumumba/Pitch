"""13th Migration

Revision ID: 52180610f13d
Revises: e0379c15e9b6
Create Date: 2018-09-07 23:11:57.663521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52180610f13d'
down_revision = 'e0379c15e9b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
