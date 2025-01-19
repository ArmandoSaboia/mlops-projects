from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from src.services.ip_validator import IPValidator
from src.services.merchant_validator import MerchantValidator
from src.services.company_validator import CompanyValidator
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Fraud Detection API",
    description="API for detecting fraudulent transactions",
    version="0.1.0"
)

# Initialize services
try:
    ip_validator = IPValidator(os.getenv("IPSTACK_API_KEY"))
    merchant_validator = MerchantValidator(os.getenv("CLEARBIT_API_KEY"))
    company_validator = CompanyValidator(os.getenv("ORB_INTELLIGENCE_API_KEY"))
except Exception as e:
    print(f"Error initializing services: {e}")

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Fraud Detection API is running"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "services": {
            "ip_validator": bool(os.getenv("IPSTACK_API_KEY")),
            "merchant_validator": bool(os.getenv("CLEARBIT_API_KEY")),
            "company_validator": bool(os.getenv("ORB_INTELLIGENCE_API_KEY"))
        }
    }
