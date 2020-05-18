"""create user table

Revision ID: caea10e30650
Revises: b2f156ae4992
Create Date: 2020-05-02 22:31:38.402834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'caea10e30650'
down_revision = 'b2f156ae4992'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('orders',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('code', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('amount', sa.DECIMAL(), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('orders')
