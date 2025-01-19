import pandas as pd
import numpy as np
from typing import Dict, List
from datetime import datetime
import holidays
from sklearn.preprocessing import LabelEncoder

class FeatureEngineer:
    def __init__(self, config: Dict):
        self.config = config
        self.label_encoders = {}
        self.us_holidays = holidays.US()
    
    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create all features for model training."""
        df = df.copy()
        
        # Time-based features
        df = self._create_time_features(df)
        
        # Amount-based features
        df = self._create_amount_features(df)
        
        # Location-based features
        df = self._create_location_features(df)
        
        # Categorical features encoding
        df = self._encode_categorical_features(df)
        
        return df
    
    def _create_time_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create time-based features."""
        df = df.copy()
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        df['is_night'] = ((df['hour'] >= 22) | (df['hour'] <= 5)).astype(int)
        df['is_holiday'] = pd.to_datetime(df['timestamp']).map(
            lambda x: x in self.us_holidays
        ).astype(int)
        return df
    
    def _create_amount_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create amount-based features."""
        # Calculate amount statistics per customer
        amount_stats = df.groupby('customer_id')['amount'].agg([
            'mean', 'std', 'max', 'min'
        ]).reset_index()
        
        df = df.merge(amount_stats, on='customer_id', how='left')
        df['amount_vs_mean'] = df['amount'] / df['mean']
        df['amount_vs_max'] = df['amount'] / df['max']
        
        return df
    
    def _create_location_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create location-based features."""
        # Calculate distance from previous transaction
        df['prev_lat'] = df.groupby('customer_id')['latitude'].shift(1)
        df['prev_lon'] = df.groupby('customer_id')['longitude'].shift(1)
        
        df['distance'] = self._calculate_distance(
            df['latitude'], df['longitude'],
            df['prev_lat'], df['prev_lon']
        )
        
        df['speed'] = df['distance'] / df.groupby('customer_id')['timestamp'].diff().dt.total_seconds()
        
        return df
    
    def _calculate_distance(self, lat1, lon1, lat2, lon2) -> pd.Series:
        """Calculate Haversine distance between coordinates."""
        R = 6371  # Earth's radius in kilometers
        
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        return R * c 