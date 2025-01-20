from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(String, primary_key=True)
    product_id = Column(String, index=True)
    warehouse_id = Column(String, index=True)
    current_stock = Column(Integer, nullable=False)
    min_stock_level = Column(Integer, nullable=False)
    max_stock_level = Column(Integer, nullable=False)
    reorder_point = Column(Integer, nullable=False)
    lead_time_days = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)

class StockMovement(Base):
    __tablename__ = 'stock_movements'
    
    id = Column(String, primary_key=True)
    product_id = Column(String, ForeignKey('inventory.product_id'))
    warehouse_id = Column(String, ForeignKey('inventory.warehouse_id'))
    movement_type = Column(String, nullable=False)  # 'in' or 'out'
    quantity = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    reference = Column(String)

class PurchaseOrder(Base):
    __tablename__ = 'purchase_orders'
    
    id = Column(String, primary_key=True)
    product_id = Column(String, ForeignKey('inventory.product_id'))
    warehouse_id = Column(String, ForeignKey('inventory.warehouse_id'))
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    expected_delivery = Column(DateTime, nullable=False)
    status = Column(String, default='pending')  # pending, delivered, cancelled
    total_cost = Column(Float) 