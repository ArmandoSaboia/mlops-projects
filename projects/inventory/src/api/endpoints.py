from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from datetime import datetime
from src.validation.inventory_validator import ProductInventory, StockMovement
from src.monitoring.inventory_monitor import InventoryMonitor
from src.forecasting.demand_predictor import DemandPredictor
import time

app = FastAPI(title="Inventory Management Service")
monitor = InventoryMonitor()

class InventoryResponse(BaseModel):
    product_id: str
    warehouse_id: str
    current_stock: int
    forecast_demand: float
    reorder_suggestion: bool
    next_delivery_date: Optional[datetime]

@app.get("/inventory/{product_id}", response_model=InventoryResponse)
async def get_inventory_status(
    product_id: str,
    warehouse_id: str = None
):
    try:
        inventory = await inventory_service.get_product_inventory(
            product_id, warehouse_id
        )
        forecast = await demand_predictor.get_forecast(product_id)
        
        return InventoryResponse(
            product_id=product_id,
            warehouse_id=warehouse_id,
            current_stock=inventory.current_stock,
            forecast_demand=forecast.next_7_days,
            reorder_suggestion=inventory.current_stock < inventory.reorder_point,
            next_delivery_date=inventory.next_delivery_date
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/inventory/movement")
async def record_stock_movement(movement: StockMovement):
    try:
        start_time = time.time()
        result = await inventory_service.process_movement(movement)
        
        # Update monitoring metrics
        monitor.update_stock_level(
            movement.product_id,
            movement.warehouse_id,
            result.new_stock_level
        )
        
        return {"status": "success", "new_stock_level": result.new_stock_level}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 