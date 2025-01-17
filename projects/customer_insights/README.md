# Customer Insights

## Overview
This project focuses on analyzing customer data to derive actionable insights.
1. **Customer segmentation**
2. **Personalized recommendations**
3. **Customer lifetime value prediction**

## Structure
- `data/`: Contains raw and processed data.
- `data_ingestion/`: Scripts for fetching data from APIs or databases.
- `features/`: Feature engineering scripts.
- `models/`: Trained models.
- `training/`: Model training scripts.
- `inference/`: API for model inference.
- `streamlit_app/`: Streamlit application for visualization.
- `tests/`: Unit and integration tests.
- `dags/`: Airflow DAGs for pipeline orchestration.

## Usage
Run the following command to start the Streamlit app:
```bash
streamlit run streamlit_app/app.py
