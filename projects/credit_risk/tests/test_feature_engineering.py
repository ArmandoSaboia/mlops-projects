import pytest
from src.preprocessing.feature_engineering import FeatureEngineer, CreditApplication

class TestFeatureEngineer:
    @pytest.fixture
    def config(self):
        return {
            'income_brackets': [30000, 60000, 100000],
            'employment_weights': {1: 0.2, 3: 0.5, 5: 0.8, 10: 1.0},
            'dti_thresholds': [0.2, 0.4, 0.6],
            'purpose_risk_scores': {
                'debt_consolidation': 0.6,
                'home_improvement': 0.3,
                'business': 0.7
            }
        }
    
    @pytest.fixture
    def engineer(self, config):
        return FeatureEngineer(config)
    
    def test_calculate_income_bracket(self, engineer):
        assert engineer._calculate_income_bracket(25000) == 0
        assert engineer._calculate_income_bracket(75000) == 2
        
    def test_score_employment(self, engineer):
        assert engineer._score_employment(2) == 0.2
        assert engineer._score_employment(7) == 0.8 