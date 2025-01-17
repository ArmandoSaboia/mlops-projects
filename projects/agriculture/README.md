[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https:)
![MIT LICENSE](https://badgen.net//badge/license/MIT/green) 
![MAINTAINED BADGE](https://img.shields.io/badge/Maintained%3F-yes-green.svg) 
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/ArmandoSaboia/mlops-projects/projects/agriculture/)
![GitHub pull requests](https://img.shields.io/github/issues-pr/mlops-projects/projects/agriculture/)
![GitHub contributors](https://img.shields.io/github/contributors/ArmandoSaboia/mlops-projects/projects/agriculture/)

# Agriculture Project

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
``` 

### Usage
Data Ingestion
Use api_client.py to fetch data from APIs. Use db_client.py to interact with databases.

### Feature Engineering
Run build_features.py to generate features. Use feature_utils.py for helper functions.

### Model Training
Train the churn model using train_churn.py. Train the recommendation model using train_recommendation.py.

### Inference
Start the FastAPI app using main.py. Use model_loader.py to load models for inference.

### Streamlit App
Run the Streamlit app using:
```bash  
streamlit run streamlit_app/app.py
```

### Testing
Run unit tests using:
```bash
pytest tests/
```

### Docker
- **Build the Docker image:**
```bash
docker build -t agriculture .
```
- **Run the container:**
```bash
docker-compose up
```

## Dependencies
Install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Contributing
- **Fork the repository.** 
- **Create a new branch for your feature or bugfix.** 
- **Submit a pull request.**

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
