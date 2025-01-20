from prometheus_client import Counter, Histogram, Gauge
from typing import Dict, List
import time

class RecommendationMonitor:
    def __init__(self):
        # Recommendation metrics
        self.recommendation_counter = Counter(
            'product_recommendations_total',
            'Total number of recommendations generated',
            ['user_segment']
        )
        
        # Response time metrics
        self.recommendation_latency = Histogram(
            'recommendation_generation_seconds',
            'Time taken to generate recommendations',
            ['model_version']
        )
        
        # Click-through rate metrics
        self.recommendation_ctr = Gauge(
            'recommendation_ctr',
            'Click-through rate for recommendations',
            ['product_category']
        )
        
        # Model performance metrics
        self.model_metrics = Gauge(
            'recommendation_model_metrics',
            'Model performance metrics',
            ['metric_name']
        )
    
    def record_recommendations(self, user_segment: str, latency: float, model_version: str):
        self.recommendation_counter.labels(user_segment=user_segment).inc()
        self.recommendation_latency.labels(model_version=model_version).observe(latency)
    
    def update_ctr(self, category: str, ctr: float):
        self.recommendation_ctr.labels(product_category=category).set(ctr) 