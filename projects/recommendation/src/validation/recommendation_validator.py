from pydantic import BaseModel, validator, constr
from typing import List, Dict, Optional
from datetime import datetime

class UserProfile(BaseModel):
    user_id: str
    preferences: List[str]
    purchase_history: List[Dict[str, str]]
    last_active: datetime
    segment: Optional[str]
    
    @validator('preferences')
    def validate_preferences(cls, v):
        if not v:
            raise ValueError('User must have at least one preference')
        return v

class RecommendationRequest(BaseModel):
    user_id: str
    n_recommendations: int
    context: Optional[Dict[str, str]]
    filters: Optional[Dict[str, List[str]]]
    
    @validator('n_recommendations')
    def validate_n_recommendations(cls, v):
        if not 1 <= v <= 100:
            raise ValueError('Number of recommendations must be between 1 and 100')
        return v

class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[Dict[str, any]]
    score: float
    generation_time: float
    model_version: str
    
    @validator('score')
    def validate_score(cls, v):
        if not 0 <= v <= 1:
            raise ValueError('Recommendation score must be between 0 and 1')
        return v 