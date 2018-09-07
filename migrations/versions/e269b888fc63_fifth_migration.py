"""Fifth Migration

Revision ID: e269b888fc63
Revises: 0a2018b95b40
Create Date: 2018-09-07 12:37:00.015130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e269b888fc63'
down_revision = '0a2018b95b40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitchs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('details', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitchs')
    # ### end Alembic commands ###