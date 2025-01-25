from typing import Dict, List, Optional
from datetime import datetime, timedelta
from src.validation.inventory_validator import ProductInventory, StockMovement
from src.database.repository import InventoryRepository
from src.forecasting.demand_predictor import DemandPredictor

class InventoryService:
    def __init__(
        self,
        repository: InventoryRepository,
        demand_predictor: DemandPredictor,
        config: Dict
    ):
        self.repository = repository
        self.demand_predictor = demand_predictor
        self.config = config
    
    async def get_product_inventory(
        self,
        product_id: str,
        warehouse_id: Optional[str] = None
    ) -> ProductInventory:
        """Get current inventory status for a product."""
        inventory = await self.repository.get_inventory(product_id, warehouse_id)
        if not inventory:
            raise ValueError(f"No inventory found for product {product_id}")
        return inventory
    
    async def process_movement(self, movement: StockMovement) -> Dict:
        """Process stock movement (in/out) and update inventory."""
        # Get current inventory
        inventory = await self.get_product_inventory(
            movement.product_id,
            movement.warehouse_id
        )
        
        # Calculate new stock level
        if movement.movement_type == 'in':
            new_level = inventory.current_stock + movement.quantity
        else:  # out
            new_level = inventory.current_stock - movement.quantity
            if new_level < 0:
                raise ValueError("Insufficient stock for movement")
        
        # Update inventory
        updated = await self.repository.update_stock_level(
            movement.product_id,
            movement.warehouse_id,
            new_level,
            movement.timestamp
        )
        
        # Check if reorder is needed
        if new_level <= inventory.reorder_point:
            await self._trigger_reorder(inventory)
        
        return {
            "new_stock_level": new_level,
            "reorder_triggered": new_level <= inventory.reorder_point
        }
    
    async def _trigger_reorder(self, inventory: ProductInventory):
        """Trigger reorder process for low stock."""
        forecast = await self.demand_predictor.get_forecast(inventory.product_id)
        optimal_order = self._calculate_optimal_order(
            inventory,
            forecast.next_lead_time_demand
        )
        
        await self.repository.create_order(
            product_id=inventory.product_id,
            warehouse_id=inventory.warehouse_id,
            quantity=optimal_order,
            expected_delivery=datetime.now() + timedelta(
                days=inventory.lead_time_days
            )
        ) 