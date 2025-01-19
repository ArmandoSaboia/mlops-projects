from pydantic import BaseModel, validator
from typing import Dict, List, Optional
from datetime import datetime

class MarketData(BaseModel):
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    indicators: Optional[Dict[str, float]]

    @validator('volume')
    def validate_volume(cls, v):
        if v < 0:
            raise ValueError('Volume must be non-negative')
        return v

    @validator('high')
    def validate_high(cls, v, values):
        if 'low' in values and v < values['low']:
            raise ValueError('High price cannot be less than low price')
        return v

class TradingSignal(BaseModel):
    symbol: str
    signal_type: str  # 'buy' or 'sell'
    confidence: float
    timestamp: datetime
    indicators_used: List[str]
    prediction_horizon: str  # '1d', '1w', '1m'

    @validator('confidence')
    def validate_confidence(cls, v):
        if not 0 <= v <= 1:
            raise ValueError('Confidence must be between 0 and 1')
        return v 