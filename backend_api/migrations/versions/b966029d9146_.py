"""empty message

Revision ID: b966029d9146
Revises: 181c04906d55
Create Date: 2022-12-08 14:52:01.314482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b966029d9146'
down_revision = '181c04906d55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group__inbox', sa.Column('group_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'group__inbox', 'chatgroups', ['group_id'], ['group_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'group__inbox', type_='foreignkey')
    op.drop_column('group__inbox', 'group_id')
    # ### end Alembic commands ###