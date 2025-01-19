from pydantic import BaseModel, validator
from typing import Dict, Optional
from datetime import datetime

class TransactionValidation(BaseModel):
    transaction_id: str
    amount: float
    merchant_id: str
    customer_id: str
    timestamp: datetime
    location: Dict[str, float]
    device_id: Optional[str]

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Amount must be positive')
        return v

    @validator('location')
    def validate_location(cls, v):
        if 'lat' not in v or 'lon' not in v:
            raise ValueError('Location must contain lat and lon')
        if not (-90 <= v['lat'] <= 90):
            raise ValueError('Invalid latitude')
        if not (-180 <= v['lon'] <= 180):
            raise ValueError('Invalid longitude')
        return v

class DataValidator:
    def __init__(self, config: Dict):
        self.config = config
        self.validation_errors = []

    def validate_transaction(self, data: Dict) -> bool:
        try:
            TransactionValidation(**data)
            return True
        except Exception as e:
            self.validation_errors.append(str(e))
            return False 