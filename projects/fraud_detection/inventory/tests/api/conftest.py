import pytest
from unittest.mock import AsyncMock, MagicMock
from src.services.inventory_service import InventoryService
from src.validation.inventory_validator import ProductInventory

@pytest.fixture
def mock_inventory_service(monkeypatch):
    mock_service = AsyncMock(spec=InventoryService)
    
    # Mock get_product_inventory
    async def mock_get_inventory(*args, **kwargs):
        return ProductInventory(
            product_id="PROD001",
            warehouse_id="WH001",
            current_stock=100,
            min_stock_level=20,
            max_stock_level=200,
            reorder_point=50,
            lead_time_days=3,
            last_updated=datetime.now()
        )
    
    mock_service.get_product_inventory = mock_get_inventory
    
    # Mock process_movement
    async def mock_process_movement(*args, **kwargs):
        return {
            "status": "success",
            "new_stock_level": 150,
            "reorder_triggered": False
        }
    
    mock_service.process_movement = mock_process_movement
    
    monkeypatch.setattr(
        "src.api.endpoints.inventory_service",
        mock_service
    )
    return mock_service 