from prometheus_client import Counter, Histogram, Gauge
from typing import Dict
import time

class OutcomeMonitor:
    def __init__(self):
        # Prediction metrics
        self.prediction_counter = Counter(
            'patient_outcome_predictions_total',
            'Total number of outcome predictions made',
            ['outcome_type']
        )
        
        self.prediction_latency = Histogram(
            'patient_outcome_prediction_seconds',
            'Time taken for outcome prediction',
            ['model_version']
        )
        
        # Accuracy metrics
        self.prediction_accuracy = Gauge(
            'patient_outcome_accuracy',
            'Rolling accuracy of outcome predictions',
            ['outcome_type', 'timeframe']
        )
        
        # Feature drift metrics
        self.feature_drift = Gauge(
            'patient_feature_drift',
            'Feature distribution drift score',
            ['feature_name']
        )
    
    def record_prediction(self, outcome_type: str, latency: float, model_version: str):
        self.prediction_counter.labels(outcome_type=outcome_type).inc()
        self.prediction_latency.labels(model_version=model_version).observe(latency)
    
    def update_accuracy(self, accuracy: float, outcome_type: str, timeframe: str):
        self.prediction_accuracy.labels(
            outcome_type=outcome_type,
            timeframe=timeframe
        ).set(accuracy) 