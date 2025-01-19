from prometheus_client import Counter, Histogram, Gauge
from typing import Dict
import time

class MetricsCollector:
    def __init__(self):
        # Prediction metrics
        self.prediction_counter = Counter(
            'fraud_predictions_total',
            'Total number of predictions'
        )
        
        # Latency metrics
        self.prediction_latency = Histogram(
            'prediction_latency_seconds',
            'Time taken for prediction'
        )
        
        # Model performance metrics
        self.model_accuracy = Gauge(
            'model_accuracy',
            'Current model accuracy'
        )
        
        # Feature drift metrics
        self.feature_drift = Gauge(
            'feature_drift',
            'Feature drift score',
            ['feature_name']
        )
    
    def record_prediction(self, prediction: int, latency: float):
        """Record a prediction and its latency."""
        self.prediction_counter.labels(
            prediction=str(prediction)
        ).inc()
        self.prediction_latency.observe(latency)
    
    def update_model_metrics(self, metrics: Dict):
        """Update model performance metrics."""
        self.model_accuracy.set(metrics['accuracy'])
        
    def record_feature_drift(self, feature_name: str, drift_score: float):
        """Record feature drift score."""
        self.feature_drift.labels(
            feature_name=feature_name
        ).set(drift_score) 