import torch
import torch.nn as nn
from typing import Dict, Tuple
import pytorch_lightning as pl

class MarketTrendPredictor(pl.LightningModule):
    def __init__(self, config: Dict):
        super().__init__()
        self.config = config
        self.lstm = nn.LSTM(
            input_size=config['input_size'],
            hidden_size=config['hidden_size'],
            num_layers=config['num_layers'],
            dropout=config['dropout'],
            batch_first=True
        )
        self.fc = nn.Linear(config['hidden_size'], config['output_size'])
        
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        predictions = self.fc(lstm_out[:, -1, :])
        return predictions
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = nn.MSELoss()(y_hat, y)
        self.log('train_loss', loss)
        return loss 