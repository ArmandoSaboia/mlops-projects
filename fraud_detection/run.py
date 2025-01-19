import uvicorn
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent)
sys.path.append(project_root)

def main():
    """Run the FastAPI application."""
    uvicorn.run(
        "src.api.endpoints:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main() 