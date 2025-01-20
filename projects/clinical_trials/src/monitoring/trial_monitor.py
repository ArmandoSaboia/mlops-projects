from prometheus_client import Counter, Gauge, Histogram
from typing import Dict
import time

class TrialMonitor:
    def __init__(self):
        # Enrollment metrics
        self.enrollment_counter = Counter(
            'clinical_trial_enrollments_total',
            'Total number of trial enrollments',
            ['trial_id', 'site_id']
        )
        
        # Adverse events
        self.adverse_events = Counter(
            'clinical_trial_adverse_events',
            'Number of adverse events reported',
            ['trial_id', 'severity']
        )
        
        # Protocol deviations
        self.protocol_deviations = Counter(
            'clinical_trial_protocol_deviations',
            'Number of protocol deviations',
            ['trial_id', 'type']
        )
        
        # Site performance
        self.site_performance = Gauge(
            'clinical_trial_site_performance',
            'Site performance metrics',
            ['trial_id', 'site_id', 'metric']
        )
    
    def record_enrollment(self, trial_id: str, site_id: str):
        self.enrollment_counter.labels(
            trial_id=trial_id,
            site_id=site_id
        ).inc()
    
    def record_adverse_event(self, trial_id: str, severity: str):
        self.adverse_events.labels(
            trial_id=trial_id,
            severity=severity
        ).inc() 