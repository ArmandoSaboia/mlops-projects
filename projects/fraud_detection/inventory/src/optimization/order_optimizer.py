import numpy as np
from typing import Dict
from dataclasses import dataclass

@dataclass
class OrderRecommendation:
    optimal_quantity: int
    safety_stock: int
    total_cost: float
    service_level: float

class OrderOptimizer:
    def __init__(self, config: Dict):
        self.config = config
        
    def calculate_optimal_order(
        self,
        current_stock: int,
        forecast_demand: float,
        lead_time: int,
        holding_cost: float,
        stockout_cost: float,
        service_level: float = 0.95
    ) -> OrderRecommendation:
        """Calculate optimal order quantity using probabilistic model."""
        # Calculate safety stock
        z_score = self._get_z_score(service_level)
        demand_std = forecast_demand * self.config['demand_uncertainty']
        safety_stock = z_score * demand_std * np.sqrt(lead_time)
        
        # Calculate EOQ (Economic Order Quantity)
        annual_demand = forecast_demand * 365
        order_cost = self.config['fixed_order_cost']
        eoq = np.sqrt(
            (2 * annual_demand * order_cost) / holding_cost
        )
        
        # Adjust for current stock and lead time demand
        lead_time_demand = forecast_demand * lead_time
        optimal_quantity = max(
            0,
            eoq + lead_time_demand + safety_stock - current_stock
        )
        
        # Calculate total cost
        total_cost = self._calculate_total_cost(
            optimal_quantity,
            holding_cost,
            order_cost,
            stockout_cost,
            lead_time_demand,
            safety_stock
        )
        
        return OrderRecommendation(
            optimal_quantity=int(np.ceil(optimal_quantity)),
            safety_stock=int(np.ceil(safety_stock)),
            total_cost=total_cost,
            service_level=service_level
        ) 