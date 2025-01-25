from prometheus_client import Counter, Gauge, Histogram
from typing import Dict
import time

class InventoryMonitor:
    def __init__(self):
        # Stock level metrics
        self.stock_level = Gauge(
            'inventory_stock_level',
            'Current stock level for each product',
            ['product_id', 'warehouse_id']
        )
        
        # Stockout metrics
        self.stockout_counter = Counter(
            'inventory_stockouts_total',
            'Total number of stockout events',
            ['product_id', 'warehouse_id']
        )
        
        # Forecast accuracy metrics
        self.forecast_accuracy = Gauge(
            'inventory_forecast_accuracy',
            'Forecast accuracy metrics',
            ['product_id', 'metric']
        )
        
        # Reorder metrics
        self.reorder_events = Counter(
            'inventory_reorders_total',
            'Total number of reorder events',
            ['product_id', 'warehouse_id', 'reason']
        )
    
    def update_stock_level(self, product_id: str, warehouse_id: str, level: int):
        self.stock_level.labels(
            product_id=product_id,
            warehouse_id=warehouse_id
        ).set(level)
        
        if level == 0:
            self.stockout_counter.labels(
                product_id=product_id,
                warehouse_id=warehouse_id
            ).inc() 