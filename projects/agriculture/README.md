# agriculture

## Overview
A brief description of the project and its purpose.

## Repository Structure
```bash
agriculture/
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
docker build -t agriculture .

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
