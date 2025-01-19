# Fraud Detection API

A machine learning-powered API for detecting fraudulent transactions.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/ArmandoSaboia/mlops-projects.git
cd projects/fraud_detection
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Set up environment variables:
Create a `.env` file in the project root with:
```
IPSTACK_API_KEY=your_ipstack_key
CLEARBIT_API_KEY=your_clearbit_key
ORB_INTELLIGENCE_API_KEY=your_orb_key
```

5. Run the API:
```bash
python run.py
```

## API Endpoints

- `GET /`: Root endpoint
- `GET /health`: Health check endpoint
- `POST /predict`: Fraud prediction endpoint

## Development

Run tests:
```bash
pytest tests/
```

## License

MIT
