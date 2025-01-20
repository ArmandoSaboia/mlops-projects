import pytest
import numpy as np
import pandas as pd
from src.model.recommender import ProductRecommender

class TestProductRecommender:
    @pytest.fixture
    def config(self):
        return {
            'model_type': 'neural_collaborative',
            'embedding_dim': 64,
            'learning_rate': 0.001,
            'batch_size': 256,
            'n_recommendations': 10,
            'similarity_metric': 'cosine'
        }
    
    @pytest.fixture
    def recommender(self, config):
        return ProductRecommender(config)
    
    def test_generate_embeddings(self, recommender):
        interactions = pd.DataFrame({
            'user_id': np.random.randint(0, 100, 1000),
            'product_id': np.random.randint(0, 50, 1000),
            'rating': np.random.uniform(1, 5, 1000)
        })
        
        user_embeddings = recommender.generate_user_embeddings(interactions)
        product_embeddings = recommender.generate_product_embeddings(interactions)
        
        assert user_embeddings.shape[1] == recommender.config['embedding_dim']
        assert product_embeddings.shape[1] == recommender.config['embedding_dim'] 