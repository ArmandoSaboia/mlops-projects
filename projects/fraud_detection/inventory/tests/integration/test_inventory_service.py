import pytest
from datetime import datetime, timedelta
from src.services.inventory_service import InventoryService
from src.database.repository import InventoryRepository
from src.forecasting.demand_predictor import DemandPredictor
from src.validation.inventory_validator import StockMovement

class TestInventoryService:
    @pytest.fixture
    async def repository(self, test_db_session):
        return InventoryRepository(test_db_session)
    
    @pytest.fixture
    def demand_predictor(self):
        return DemandPredictor({'model_path': 'test/model'})
    
    @pytest.fixture
    def service(self, repository, demand_predictor):
        config = {
            'reorder_threshold': 0.2,
            'max_order_quantity': 1000
        }
        return InventoryService(repository, demand_predictor, config)
    
    async def test_process_movement_in(self, service):
        # Arrange
        movement = StockMovement(
            movement_id="test_mov_1",
            product_id="PROD001",
            warehouse_id="WH001",
            movement_type="in",
            quantity=100,
            timestamp=datetime.now(),
            reference="TEST-REF-001"
        )
        
        # Act
        result = await service.process_movement(movement)
        
        # Assert
        assert result['status'] == 'success'
        assert result['new_stock_level'] > 0
        
    async def test_process_movement_insufficient_stock(self, service):
        # Arrange
        movement = StockMovement(
            movement_id="test_mov_2",
            product_id="PROD001",
            warehouse_id="WH001",
            movement_type="out",
            quantity=99999,  # Very large quantity
            timestamp=datetime.now(),
            reference="TEST-REF-002"
        )
        
        # Act/Assert
        with pytest.raises(ValueError, match="Insufficient stock"):
            await service.process_movement(movement) 