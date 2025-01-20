from pydantic import BaseModel, validator, constr
from typing import List, Dict, Optional
from datetime import datetime

class ProductInventory(BaseModel):
    product_id: str
    warehouse_id: str
    current_stock: int
    min_stock_level: int
    max_stock_level: int
    reorder_point: int
    lead_time_days: int
    last_updated: datetime
    
    @validator('current_stock', 'min_stock_level', 'max_stock_level')
    def validate_stock_levels(cls, v):
        if v < 0:
            raise ValueError('Stock levels cannot be negative')
        return v
    
    @validator('max_stock_level')
    def validate_max_stock(cls, v, values):
        if 'min_stock_level' in values and v <= values['min_stock_level']:
            raise ValueError('Max stock must be greater than min stock')
        return v

class StockMovement(BaseModel):
    movement_id: str
    product_id: str
    warehouse_id: str
    movement_type: str  # 'in' or 'out'
    quantity: int
    timestamp: datetime
    reference: Optional[str]
    
    @validator('movement_type')
    def validate_movement_type(cls, v):
        if v not in ['in', 'out']:
            raise ValueError('Movement type must be either "in" or "out"')
        return v
    
    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be positive')
        return v 