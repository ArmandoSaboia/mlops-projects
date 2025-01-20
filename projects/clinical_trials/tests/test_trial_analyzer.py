import pytest
import pandas as pd
import numpy as np
from src.analysis.trial_analyzer import TrialAnalyzer
from datetime import datetime, timedelta

class TestTrialAnalyzer:
    @pytest.fixture
    def config(self):
        return {
            'metrics': ['efficacy', 'safety', 'adherence'],
            'significance_level': 0.05,
            'min_sample_size': 30,
            'treatment_groups': ['control', 'treatment_a', 'treatment_b']
        }
    
    @pytest.fixture
    def analyzer(self, config):
        return TrialAnalyzer(config)
    
    def test_calculate_efficacy(self, analyzer):
        trial_data = pd.DataFrame({
            'group': ['control', 'treatment_a'] * 50,
            'outcome': np.random.binomial(1, [0.3] * 50 + [0.7] * 50),
            'adherence': np.random.uniform(0.8, 1.0, 100)
        })
        
        results = analyzer.calculate_efficacy(trial_data)
        assert 'p_value' in results
        assert 'effect_size' in results
        assert 'confidence_interval' in results 