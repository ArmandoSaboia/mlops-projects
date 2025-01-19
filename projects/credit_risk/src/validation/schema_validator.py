from pydantic import BaseModel, validator, constr
from typing import Optional, List
from datetime import date

class ApplicantInfo(BaseModel):
    first_name: constr(min_length=2, max_length=50)
    last_name: constr(min_length=2, max_length=50)
    date_of_birth: date
    ssn: constr(regex=r'^\d{3}-\d{2}-\d{4}$')
    email: constr(regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class FinancialInfo(BaseModel):
    annual_income: float
    employment_length: int
    debt_to_income: float
    monthly_expenses: float
    existing_loans: List[dict]

    @validator('annual_income')
    def validate_income(cls, v):
        if v < 0:
            raise ValueError('Income must be non-negative')
        if v > 10_000_000:
            raise ValueError('Income seems unreasonably high')
        return v

    @validator('debt_to_income')
    def validate_dti(cls, v):
        if not 0 <= v <= 1:
            raise ValueError('Debt-to-income ratio must be between 0 and 1')
        return v 