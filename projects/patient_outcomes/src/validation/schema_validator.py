from pydantic import BaseModel, validator, constr
from typing import Dict, List, Optional
from datetime import datetime

class PatientDemographics(BaseModel):
    patient_id: str
    age: int
    gender: str
    ethnicity: Optional[str]
    admission_date: datetime
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 120:
            raise ValueError('Age must be between 0 and 120')
        return v
    
    @validator('gender')
    def validate_gender(cls, v):
        valid_genders = ['M', 'F', 'O']
        if v not in valid_genders:
            raise ValueError(f'Gender must be one of {valid_genders}')
        return v

class VitalSigns(BaseModel):
    heart_rate: float
    blood_pressure_systolic: float
    blood_pressure_diastolic: float
    temperature: float
    respiratory_rate: float
    oxygen_saturation: float
    timestamp: datetime
    
    @validator('heart_rate')
    def validate_heart_rate(cls, v):
        if not 20 <= v <= 300:
            raise ValueError('Heart rate must be between 20 and 300')
        return v
    
    @validator('oxygen_saturation')
    def validate_oxygen_saturation(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Oxygen saturation must be between 0 and 100')
        return v 