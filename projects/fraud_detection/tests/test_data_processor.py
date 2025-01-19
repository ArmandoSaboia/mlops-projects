import pytest
from src.preprocessing.data_processor import DataProcessor, TransactionFeatures
import pandas as pd

class TestDataProcessor:
    @pytest.fixture
    def config(self):
        return {
            'amount_mean': 1000.0,
            'amount_std': 500.0,
            'high_risk_merchants': ['merchant123', 'merchant456']
        }
    
    @pytest.fixture
    def processor(self, config):
        return DataProcessor(config)
    
    def test_normalize_amount(self, processor):
        amount = 2000.0
        expected = 2.0  # (2000 - 1000) / 500
        assert processor._normalize_amount(amount) == expected
    
    def test_process_transaction(self, processor):
        transaction = TransactionFeatures(
            amount=1500.0,
            merchant_id='merchant123',
            customer_id='customer789',
            timestamp='2024-03-15T10:30:00Z',
            location={'lat': 40.7128, 'lon': -74.0060},
            device_id='device456'
        )
        result = processor.process_transaction(transaction)
        assert isinstance(result, pd.DataFrame)
        assert len(result.columns) == 6 