from typing import Dict, List
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class MarketDataCollector:
    def __init__(self, config: Dict):
        self.config = config
        self.symbols = config['symbols']
        
    def fetch_market_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch market data for analysis."""
        all_data = []
        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            data = ticker.history(start=start_date, end=end_date)
            data['Symbol'] = symbol
            all_data.append(data)
            
        return pd.concat(all_data)
    
    def calculate_technical_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate technical indicators for market analysis."""
        # Moving averages
        df['MA20'] = df.groupby('Symbol')['Close'].rolling(window=20).mean().reset_index(0, drop=True)
        df['MA50'] = df.groupby('Symbol')['Close'].rolling(window=50).mean().reset_index(0, drop=True)
        
        # RSI
        df['RSI'] = self._calculate_rsi(df)
        
        # MACD
        df['MACD'] = self._calculate_macd(df)
        
        return df 