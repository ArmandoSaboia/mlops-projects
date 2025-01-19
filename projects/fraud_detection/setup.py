from setuptools import setup, find_packages

setup(
    name="fraud_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn[standard]>=0.15.0",
        "scikit-learn>=0.24.2",
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "prometheus-client>=0.19.0",
        "pytest>=6.2.5",
        "python-dotenv>=0.19.0",
        "joblib>=1.3.2",
    ],
    python_requires=">=3.8",
) 