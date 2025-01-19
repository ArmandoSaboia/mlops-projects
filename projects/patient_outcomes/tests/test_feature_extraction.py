import pytest
import pandas as pd
import numpy as np
from src.features.feature_extractor import PatientFeatureExtractor

class TestPatientFeatureExtractor:
    @pytest.fixture
    def config(self):
        return {
            'vital_signs': ['heart_rate', 'blood_pressure', 'temperature'],
            'lab_tests': ['wbc_count', 'glucose', 'creatinine'],
            'time_windows': [24, 48, 72],  # hours
            'aggregation_methods': ['mean', 'max', 'min', 'std']
        }
    
    @pytest.fixture
    def extractor(self, config):
        return PatientFeatureExtractor(config)
    
    def test_extract_temporal_features(self, extractor):
        # Create sample patient data
        data = pd.DataFrame({
            'timestamp': pd.date_range(start='2024-01-01', periods=10, freq='H'),
            'heart_rate': np.random.normal(75, 5, 10),
            'blood_pressure': np.random.normal(120, 10, 10)
        })
        
        features = extractor.extract_temporal_features(data)
        assert 'heart_rate_24h_mean' in features.columns
        assert 'blood_pressure_24h_max' in features.columns 