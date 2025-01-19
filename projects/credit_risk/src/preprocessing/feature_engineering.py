import pandas as pd
import numpy as np
from typing import Dict, List
from pydantic import BaseModel

class CreditApplication(BaseModel):
    applicant_id: str
    income: float
    employment_length: int
    debt_to_income: float
    credit_score: int
    loan_amount: float
    loan_purpose: str
    
class FeatureEngineer:
    def __init__(self, config: Dict):
        self.config = config
        
    def create_features(self, application: CreditApplication) -> pd.DataFrame:
        """Generate features for credit risk assessment."""
        features = {
            'income_bracket': self._calculate_income_bracket(application.income),
            'employment_score': self._score_employment(application.employment_length),
            'dti_risk': self._assess_dti_risk(application.debt_to_income),
            'credit_rating': self._normalize_credit_score(application.credit_score),
            'loan_amount_risk': self._calculate_loan_risk(application.loan_amount),
            'purpose_risk': self._get_purpose_risk(application.loan_purpose)
        }
        return pd.DataFrame([features]) 