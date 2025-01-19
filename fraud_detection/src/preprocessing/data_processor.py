import pandas as pd
import numpy as np
from typing import Dict
from sklearn.preprocessing import StandardScaler
from datetime import datetime

class DataProcessor:
    def __init__(self, config: Dict):
        self.config = config
        self.scaler = StandardScaler()
        
    def preprocess_transaction(self, transaction: Dict) -> np.ndarray:
        """Process a single transaction for prediction."""
        features = self._extract_features(transaction)
        scaled_features = self._scale_features(features)
        return scaled_features
    
    def _extract_features(self, transaction: Dict) -> pd.Series:
        """Extract features from transaction data."""
        features = {
            'amount': float(transaction['amount']),
            'hour_of_day': datetime.fromisoformat(transaction['timestamp']).hour,
            'is_weekend': datetime.fromisoformat(transaction['timestamp']).weekday() >= 5,
            'merchant_category': int(transaction['merchant_category']),
            'card_present': bool(transaction['card_present'])
        }
        return pd.Series(features)
    
    def _scale_features(self, features: pd.Series) -> np.ndarray:
        """Scale features using trained scaler."""
        return self.scaler.transform(features.values.reshape(1, -1))