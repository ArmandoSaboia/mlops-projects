from typing import Dict, List, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, insert
from src.database.models import Inventory, StockMovement, PurchaseOrder
from src.validation.inventory_validator import ProductInventory
import uuid

class InventoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_inventory(
        self,
        product_id: str,
        warehouse_id: Optional[str] = None
    ) -> ProductInventory:
        """Get current inventory for a product."""
        query = select(Inventory).where(Inventory.product_id == product_id)
        if warehouse_id:
            query = query.where(Inventory.warehouse_id == warehouse_id)
        
        result = await self.session.execute(query)
        inventory = result.scalar_one_or_none()
        
        if not inventory:
            return None
            
        return ProductInventory(
            product_id=inventory.product_id,
            warehouse_id=inventory.warehouse_id,
            current_stock=inventory.current_stock,
            min_stock_level=inventory.min_stock_level,
            max_stock_level=inventory.max_stock_level,
            reorder_point=inventory.reorder_point,
            lead_time_days=inventory.lead_time_days,
            last_updated=inventory.last_updated
        )
    
    async def update_stock_level(
        self,
        product_id: str,
        warehouse_id: str,
        new_level: int,
        timestamp: datetime
    ) -> bool:
        """Update stock level for a product."""
        stmt = (
            update(Inventory)
            .where(
                Inventory.product_id == product_id,
                Inventory.warehouse_id == warehouse_id
            )
            .values(
                current_stock=new_level,
                last_updated=timestamp
            )
        )
        
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0 

    async def create_purchase_order(
        self,
        product_id: str,
        warehouse_id: str,
        quantity: int,
        expected_delivery: datetime,
        total_cost: float
    ) -> str:
        """Create a new purchase order."""
        order = PurchaseOrder(
            id=str(uuid.uuid4()),
            product_id=product_id,
            warehouse_id=warehouse_id,
            quantity=quantity,
            expected_delivery=expected_delivery,
            total_cost=total_cost
        )
        
        self.session.add(order)
        await self.session.commit()
        return order.id

    async def get_stock_movements(
        self,
        product_id: str,
        start_date: datetime,
        end_date: datetime
    ) -> List[StockMovement]:
        """Get stock movements for a product within a date range."""
        query = (
            select(StockMovement)
            .where(
                StockMovement.product_id == product_id,
                StockMovement.timestamp.between(start_date, end_date)
            )
            .order_by(StockMovement.timestamp.desc())
        )
        
        result = await self.session.execute(query)
        return result.scalars().all() 