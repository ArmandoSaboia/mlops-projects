import uvicorn
from pathlib import Path
import sys

# Add the src directory to Python path
src_path = str(Path(__file__).parent / "src")
sys.path.append(src_path)

if __name__ == "__main__":
    uvicorn.run("api.endpoints:app", host="0.0.0.0", port=8000, reload=True) 