from prometheus_client import Counter, Gauge, Histogram
from typing import Dict
import time

class SegmentationMonitor:
    def __init__(self):
        # Segment distribution metrics
        self.segment_size = Gauge(
            'customer_segment_size',
            'Number of customers in each segment',
            ['segment_id']
        )
        
        # Segment characteristics
        self.segment_metrics = Gauge(
            'customer_segment_metrics',
            'Average metrics for each segment',
            ['segment_id', 'metric']
        )
        
        # Model performance metrics
        self.silhouette_score = Gauge(
            'segmentation_silhouette_score',
            'Silhouette score of the clustering model'
        )
        
        # Processing metrics
        self.processing_time = Histogram(
            'segmentation_processing_seconds',
            'Time taken for segmentation processing',
            ['operation']
        )
    
    def update_segment_sizes(self, segment_counts: Dict[str, int]):
        for segment_id, count in segment_counts.items():
            self.segment_size.labels(segment_id=segment_id).set(count)
    
    def record_segment_metrics(self, segment_id: str, metrics: Dict[str, float]):
        for metric_name, value in metrics.items():
            self.segment_metrics.labels(
                segment_id=segment_id,
                metric=metric_name
            ).set(value) 