import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from typing import Dict, Tuple
import logging

class ModelTrainer:
    def __init__(self, config: Dict):
        self.config = config
        self.model = RandomForestClassifier(
            n_estimators=config['n_estimators'],
            max_depth=config['max_depth'],
            random_state=42
        )
        
    def train(self, X: pd.DataFrame, y: pd.Series) -> Dict:
        """Train the fraud detection model."""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Evaluate
        train_score = self.model.score(X_train, y_train)
        test_score = self.model.score(X_test, y_test)
        
        # Generate detailed metrics
        y_pred = self.model.predict(X_test)
        metrics = classification_report(y_test, y_pred, output_dict=True)
        
        return {
            'train_score': train_score,
            'test_score': test_score,
            'metrics': metrics
        }
    
    def save_model(self, path: str):
        """Save the trained model."""
        joblib.dump(self.model, path)
    
    def load_model(self, path: str):
        """Load a trained model."""
        self.model = joblib.load(path) 