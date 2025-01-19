import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from src.preprocessing.feature_engineer import FeatureEngineer

class TestFeatureEngineer:
    @pytest.fixture
    def sample_data(self):
        """Create sample transaction data."""
        return pd.DataFrame({
            'transaction_id': range(100),
            'customer_id': np.random.randint(1, 10, 100),
            'amount': np.random.uniform(10, 1000, 100),
            'timestamp': [
                datetime.now() - timedelta(hours=x)
                for x in range(100)
            ],
            'latitude': np.random.uniform(30, 45, 100),
            'longitude': np.random.uniform(-120, -70, 100),
            'merchant_category': np.random.choice(['retail', 'online', 'atm'], 100)
        })

    @pytest.fixture
    def feature_engineer(self):
        """Create feature engineer instance."""
        config = {
            'categorical_features': ['merchant_category'],
            'numerical_features': ['amount']
        }
        return FeatureEngineer(config)

    def test_time_features(self, feature_engineer, sample_data):
        """Test time-based feature creation."""
        processed_data = feature_engineer._create_time_features(sample_data)
        
        assert 'hour' in processed_data.columns
        assert 'day_of_week' in processed_data.columns
        assert 'is_weekend' in processed_data.columns
        assert processed_data['is_weekend'].isin([0, 1]).all()
