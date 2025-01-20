import pytest
from datetime import datetime, timedelta
from src.data_pipeline.market_data_collector import MarketDataCollector
import pandas as pd

class TestMarketDataCollector:
    @pytest.fixture
    def config(self):
        return {
            'symbols': ['AAPL', 'GOOGL', 'MSFT'],
            'indicators': ['MA20', 'MA50', 'RSI', 'MACD'],
            'timeframes': ['1d', '1h', '15min']
        }
    
    @pytest.fixture
    def collector(self, config):
        return MarketDataCollector(config)
    
    def test_calculate_technical_indicators(self, collector):
        # Create sample data
        data = pd.DataFrame({
            'Close': [100, 102, 98, 103, 105],
            'Symbol': ['AAPL'] * 5
        })
        
        result = collector.calculate_technical_indicators(data)
        assert 'MA20' in result.columns
        assert 'RSI' in result.columns
        assert 'MACD' in result.columns 