# Inventory Management System

A robust inventory management system built with FastAPI, SQLAlchemy, and PostgreSQL. The system provides real-time inventory tracking, demand forecasting, and automated reordering capabilities.

## Features

- Real-time inventory tracking across multiple warehouses
- Automated reorder point calculation and purchase order generation
- Demand forecasting using machine learning models
- Stock movement tracking and validation
- Comprehensive monitoring and alerting system
- RESTful API with async support

## Project Structure

```
inventory/
├── alembic/                 # Database migrations
├── src/
│   ├── api/                # FastAPI endpoints
│   ├── database/           # Database models and repository
│   ├── forecasting/        # Demand prediction models
│   ├── monitoring/         # Prometheus metrics
│   ├── optimization/       # Order optimization logic
│   ├── services/           # Business logic
│   └── validation/         # Pydantic models
├── tests/
│   ├── api/               # API endpoint tests
│   ├── integration/       # Integration tests
│   └── unit/             # Unit tests
└── config/
    ├── deployment/        # Kubernetes/Docker configs
    └── monitoring/        # Grafana dashboards
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/ArmandoSaboia/inventory-management.git
cd inventory-management
```

2. Set up the environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure the database:
```bash
# Set environment variables
export DATABASE_URL="postgresql://user:password@localhost:5432/inventory"
export REDIS_URL="redis://localhost:6379"

# Run migrations
alembic upgrade head
```

4. Start the service:
```bash
uvicorn src.api.endpoints:app --reload
```

## API Documentation

Once running, visit `http://localhost:8000/docs` for the interactive API documentation.

Key endpoints:
- `GET /inventory/{product_id}` - Get current inventory status
- `POST /inventory/movement` - Record stock movement
- `GET /inventory/forecast/{product_id}` - Get demand forecast
- `POST /inventory/orders` - Create purchase order

## Testing

Run the test suite:
```bash
pytest tests/
```

## Monitoring

The system exports Prometheus metrics and includes pre-configured Grafana dashboards for:
- Stock levels by warehouse
- Stockout events
- Forecast accuracy
- Reorder patterns

## Deployment

Kubernetes manifests are provided in `config/deployment/`. Deploy using:
```bash
kubectl apply -f config/deployment/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 