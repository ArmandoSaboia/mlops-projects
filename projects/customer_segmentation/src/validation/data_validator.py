from pydantic import BaseModel, validator, constr
from typing import List, Dict, Optional
from datetime import datetime

class CustomerProfile(BaseModel):
    customer_id: str
    registration_date: datetime
    last_purchase_date: datetime
    total_purchases: int
    total_spend: float
    product_categories: List[str]
    demographics: Optional[Dict[str, str]]
    
    @validator('total_purchases')
    def validate_purchases(cls, v):
        if v < 0:
            raise ValueError('Total purchases must be non-negative')
        return v
    
    @validator('total_spend')
    def validate_spend(cls, v):
        if v < 0:
            raise ValueError('Total spend must be non-negative')
        return v
    
    @validator('last_purchase_date')
    def validate_dates(cls, v, values):
        if 'registration_date' in values and v < values['registration_date']:
            raise ValueError('Last purchase date cannot be before registration date')
        return v

class SegmentationFeatures(BaseModel):
    recency: int  # days
    frequency: int
    monetary: float
    avg_basket_size: float
    product_diversity: int
    
    @validator('recency')
    def validate_recency(cls, v):
        if v < 0:
            raise ValueError('Recency must be non-negative')
        return v 