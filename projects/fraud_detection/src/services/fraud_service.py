from typing import Dict
import numpy as np
from datetime import datetime
import joblib

from src.preprocessing.data_processor import DataProcessor
from src.monitoring.metrics_collector import MetricsCollector

class FraudDetectionService:
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.data_processor = DataProcessor(self.config)
        self.metrics = MetricsCollector()
        self.model = self._load_model()

    def _load_model(self):
        """Load the trained model."""
        model_path = self.config.get('model_path', 'models/fraud_detector.joblib')
        try:
            return joblib.load(model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {str(e)}")

    async def predict_transaction(self, transaction: Dict) -> Dict:
        """Placeholder for fraud detection logic."""
        return {
            "fraud_probability": 0.0,
            "prediction": 0,
            "risk_factors": {}
        }

    def _get_risk_factors(self, features: np.ndarray, probability: float) -> Dict[str, float]:
        """Calculate risk factors contributing to the prediction."""
        feature_importance = self.model.feature_importances_
        risk_factors = {}
        
        for idx, importance in enumerate(feature_importance):
            if importance * probability > 0.1:  # Only include significant factors
                risk_factors[f'factor_{idx}'] = float(importance * probability)
        
        return risk_factors 