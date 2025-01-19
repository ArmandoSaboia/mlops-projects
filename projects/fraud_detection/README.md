# Fraud Detection System

A machine learning-based fraud detection system that uses real-time transaction monitoring and adaptive learning to identify potentially fraudulent activities.

## Features

- Real-time transaction scoring
- Adaptive model retraining
- Anomaly detection
- Feature engineering pipeline
- Model monitoring and drift detection
- RESTful API endpoints
- Comprehensive logging and alerting

## Project Structure

```
fraud_detection/
├── src/
│   ├── api/                # FastAPI endpoints
│   ├── preprocessing/      # Data processing and feature engineering
│   ├── training/          # Model training and evaluation
│   ├── monitoring/        # Model monitoring and metrics
│   └── utils/            # Helper functions
├── tests/                # Test suites
├── config/              # Configuration files
└── models/             # Trained model artifacts
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/ArmandoSaboia/fraud-detection.git
cd fraud-detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run the service:
```bash
uvicorn src.api.endpoints:app --reload
```

## API Documentation

Visit `http://localhost:8000/docs` for the interactive API documentation.

Key endpoints:
- `POST /predict` - Score a transaction
- `POST /feedback` - Submit feedback for model updating
- `GET /metrics` - Get model performance metrics

## Model Training

To train a new model:
```bash
python -m src.training.model_trainer
```

## Testing

Run tests:
```bash
pytest tests/
```

## License

MIT License
