from pydantic import BaseModel, validator, constr
from typing import List, Optional, Dict
from datetime import datetime, date

class PatientEligibility(BaseModel):
    patient_id: str
    age: int
    medical_history: List[str]
    current_medications: List[str]
    lab_results: Dict[str, float]
    exclusion_criteria: List[str]
    
    @validator('age')
    def validate_age(cls, v):
        if v < 18:
            raise ValueError('Patient must be 18 or older')
        return v

class TrialEvent(BaseModel):
    event_id: str
    trial_id: str
    patient_id: str
    event_type: str
    event_date: datetime
    severity: Optional[str]
    description: str
    reported_by: str
    
    @validator('event_type')
    def validate_event_type(cls, v):
        valid_types = ['adverse_event', 'protocol_deviation', 'milestone']
        if v not in valid_types:
            raise ValueError(f'Event type must be one of {valid_types}')
        return v
    
    @validator('severity')
    def validate_severity(cls, v):
        if v:
            valid_severities = ['mild', 'moderate', 'severe']
            if v not in valid_severities:
                raise ValueError(f'Severity must be one of {valid_severities}')
        return v 