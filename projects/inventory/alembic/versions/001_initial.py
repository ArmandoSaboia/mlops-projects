"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2024-03-15 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create inventory table
    op.create_table(
        'inventory',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('product_id', sa.String(), nullable=False),
        sa.Column('warehouse_id', sa.String(), nullable=False),
        sa.Column('current_stock', sa.Integer(), nullable=False),
        sa.Column('min_stock_level', sa.Integer(), nullable=False),
        sa.Column('max_stock_level', sa.Integer(), nullable=False),
        sa.Column('reorder_point', sa.Integer(), nullable=False),
        sa.Column('lead_time_days', sa.Integer(), nullable=False),
        sa.Column('last_updated', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create indices
    op.create_index('ix_inventory_product_id', 'inventory', ['product_id'])
    op.create_index('ix_inventory_warehouse_id', 'inventory', ['warehouse_id'])

def downgrade():
    op.drop_index('ix_inventory_warehouse_id')
    op.drop_index('ix_inventory_product_id')
    op.drop_table('inventory') 