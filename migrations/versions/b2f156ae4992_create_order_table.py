"""create order table

Revision ID: b2f156ae4992
Revises: caea10e30650
Create Date: 2020-05-02 22:31:56.689722

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'b2f156ae4992'
down_revision = 'caea10e30650'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('orders',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('code', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('amount_cents', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('identity', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('orders')
