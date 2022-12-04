"""empty message

Revision ID: 181c04906d55
Revises: b27371497517
Create Date: 2022-12-02 12:47:15.165893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '181c04906d55'
down_revision = 'b27371497517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chatgroups', sa.Column('group_identifier', sa.String(length=20), nullable=False))
    op.create_unique_constraint(None, 'chatgroups', ['group_identifier'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chatgroups', type_='unique')
    op.drop_column('chatgroups', 'group_identifier')
    # ### end Alembic commands ###