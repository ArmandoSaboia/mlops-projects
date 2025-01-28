from setuptools import setup, find_packages

setup(
    name="fraud_detection",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "scikit-learn==1.3.2",
        "pandas==2.1.3",
        "numpy==1.26.2",
        "prometheus-client==0.19.0",
        "pytest==7.4.3",
        "python-dotenv==1.0.0",
        "joblib==1.3.2",
        "pyyaml==6.0.1",
        "holidays>=0.36" 
    ],
)
