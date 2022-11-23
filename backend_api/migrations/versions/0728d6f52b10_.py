"""empty message

Revision ID: 0728d6f52b10
Revises: cbe705506641
Create Date: 2022-11-23 09:37:26.239915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0728d6f52b10'
down_revision = 'cbe705506641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend__request',
    sa.Column('request_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('request_sent_by', sa.Integer(), nullable=True),
    sa.Column('request_sent_to', sa.Integer(), nullable=True),
    sa.Column('request_status', sa.Enum('P', 'A', 'R'), nullable=False),
    sa.Column('request_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['request_sent_by'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['request_sent_to'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('request_id')
    )
    op.add_column('user', sa.Column('user_num_of_friends', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_num_of_friends')
    op.drop_table('friend__request')
    # ### end Alembic commands ###
