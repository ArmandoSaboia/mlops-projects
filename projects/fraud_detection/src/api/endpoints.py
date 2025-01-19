from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime
import time

from src.services.fraud_service import FraudDetectionService
from src.monitoring.metrics_collector import MetricsCollector

# Load configuration
config = {
    'model_path': 'models/fraud_detector.joblib',
    'threshold': 0.5,
    'feature_config': {
        'numerical_features': ['amount', 'hour', 'distance'],
        'categorical_features': ['merchant_category', 'merchant_country']
    }
}

# Initialize services
fraud_service = FraudDetectionService(config)
metrics = MetricsCollector()

app = FastAPI(title="Fraud Detection Service")

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    timestamp: datetime
    merchant_category: int
    merchant_country: str
    card_present: bool
    latitude: Optional[float]
    longitude: Optional[float]

class PredictionResponse(BaseModel):
    transaction_id: str
    fraud_probability: float
    prediction: int
    processing_time: float
    risk_factors: Dict[str, float]

@app.post("/predict", response_model=PredictionResponse)
async def predict_fraud(transaction: Transaction):
    try:
        start_time = time.time()
        
        # Get prediction
        result = await fraud_service.predict_transaction(transaction.dict())
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        # Record metrics
        metrics.record_prediction(
            prediction=result['prediction'],
            latency=processing_time
        )
        
        return PredictionResponse(
            transaction_id=transaction.transaction_id,
            fraud_probability=result['fraud_probability'],
            prediction=result['prediction'],
            processing_time=processing_time,
            risk_factors=result['risk_factors']
        )
    except Exception as e:
        metrics.record_error("prediction_error")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/metrics")
async def get_metrics():
    """Get current model metrics."""
    return {
        "total_predictions": metrics.prediction_counter._value.get(),
        "average_latency": metrics.prediction_latency._sum.get() / max(metrics.prediction_latency._count.get(), 1),
        "error_rate": metrics.error_counter._value.get() / max(metrics.prediction_counter._value.get(), 1)
    }
