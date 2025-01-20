import pytest
import pandas as pd
import numpy as np
from src.clustering.segmentation_model import CustomerSegmentation

class TestCustomerSegmentation:
    @pytest.fixture
    def config(self):
        return {
            'features': [
                'recency', 'frequency', 'monetary',
                'avg_basket_size', 'product_categories'
            ],
            'n_clusters': 5,
            'scaling_method': 'standard',
            'random_state': 42
        }
    
    @pytest.fixture
    def segmentation(self, config):
        return CustomerSegmentation(config)
    
    def test_preprocess_features(self, segmentation):
        data = pd.DataFrame({
            'recency': np.random.randint(1, 365, 100),
            'frequency': np.random.randint(1, 50, 100),
            'monetary': np.random.uniform(10, 1000, 100),
            'avg_basket_size': np.random.uniform(1, 10, 100),
            'product_categories': np.random.randint(1, 10, 100)
        })
        
        processed = segmentation.preprocess_features(data)
        assert processed.shape == data.shape
        assert not processed.isnull().any().any() 