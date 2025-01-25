import pytest
import pandas as pd
import numpy as np
from src.forecasting.demand_predictor import DemandPredictor
from datetime import datetime, timedelta

class TestDemandPredictor:
    @pytest.fixture
    def config(self):
        return {
            'model_type': 'lightgbm',
            'forecast_horizon': 14,  # days
            'features': [
                'historical_demand',
                'seasonality',
                'price',
                'promotions',
                'events'
            ],
            'seasonality_period': 7
        }
    
    @pytest.fixture
    def predictor(self, config):
        return DemandPredictor(config)
    
    def test_feature_generation(self, predictor):
        # Create sample historical data
        dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
        data = pd.DataFrame({
            'date': dates,
            'demand': np.random.normal(100, 20, 100),
            'price': np.random.uniform(10, 20, 100),
            'promotion': np.random.choice([0, 1], 100)
        })
        
        features = predictor.generate_features(data)
        assert 'historical_demand_7d_mean' in features.columns
        assert 'seasonality_factor' in features.columns 