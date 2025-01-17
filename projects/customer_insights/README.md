<<<<<<< HEAD
# customer insights

## Overview
A brief description of the project and its purpose.

## Repository Structure
```bash
customer_insights/
├── data/                     
│   ├── raw/                
│   └── processed/           
├── data_ingestion/           
│   ├── api_client.py        
│   └── db_client.py         
├── features/                 
│   ├── build_features.py    
│   └── feature_utils.py     
├── models/                   
│   ├── churn_model.pkl     
│   └── recommendation_model.pkl 
├── training/             
│   ├── train_churn.py      
│   └── train_recommendation.py 
├── inference/                
│   ├── main.py              
│   └── model_loader.py      
├── streamlit_app/          
│   ├── app.py               
│   └── utils.py             
├── tests/                  
│   ├── test_api.py          
│   └── test_features.py     
├── docker-compose.yml        
├── Dockerfile                  
├── requirements.txt            
├── pyproject.toml           
├── README.md               
├── .gitignore                
└── dags/                  
    └── data_pipeline.py     
    
Usage

Data Ingestion

Use api_client.py to fetch data from APIs. Use db_client.py to interact with databases.

Feature Engineering

Run build_features.py to generate features. Use feature_utils.py for helper functions.

Model Training

Train the churn model using train_churn.py. Train the recommendation model using train_recommendation.py.

Inference

Start the FastAPI app using main.py. Use model_loader.py to load models for inference.

Streamlit App

Run the Streamlit app using:
```  
streamlit run streamlit_app/app.py

Testing

Run unit tests using:

```
pytest tests/

Docker

Build the Docker image:

```
docker build -t customer_insights .

Run the container:
```
docker-compose up

Dependencies

Install the required dependencies using:
```
pip install -r requirements.txt

Contributing

Fork the repository. Create a new branch for your feature or bugfix. Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
=======
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
>>>>>>> c1acb5bc2af1113e378cc7d34faa9bc9afb008ae
