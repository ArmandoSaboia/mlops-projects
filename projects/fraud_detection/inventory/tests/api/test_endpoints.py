import pytest
from httpx import AsyncClient
from datetime import datetime
from src.api.endpoints import app
from src.validation.inventory_validator import StockMovement

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

class TestInventoryEndpoints:
    async def test_get_inventory_status(self, client, mock_inventory_service):
        # Arrange
        product_id = "PROD001"
        warehouse_id = "WH001"
        
        # Act
        response = await client.get(
            f"/inventory/{product_id}",
            params={"warehouse_id": warehouse_id}
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["product_id"] == product_id
        assert data["warehouse_id"] == warehouse_id
        assert "current_stock" in data
        assert "forecast_demand" in data
    
    async def test_record_stock_movement(self, client, mock_inventory_service):
        # Arrange
        movement = {
            "movement_id": "MOV001",
            "product_id": "PROD001",
            "warehouse_id": "WH001",
            "movement_type": "in",
            "quantity": 100,
            "timestamp": datetime.now().isoformat(),
            "reference": "TEST-REF-001"
        }
        
        # Act
        response = await client.post("/inventory/movement", json=movement)
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "new_stock_level" in data
    
    async def test_invalid_movement_type(self, client):
        # Arrange
        movement = {
            "movement_id": "MOV002",
            "product_id": "PROD001",
            "warehouse_id": "WH001",
            "movement_type": "invalid",  # Invalid movement type
            "quantity": 100,
            "timestamp": datetime.now().isoformat(),
            "reference": "TEST-REF-002"
        }
        
        # Act
        response = await client.post("/inventory/movement", json=movement)
        
        # Assert
        assert response.status_code == 422  # Validation error 