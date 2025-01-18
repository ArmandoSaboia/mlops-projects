# MLOps Projects Repository

A comprehensive collection of 18 production-ready MLOps projects implementing end-to-end machine learning solutions across various domains.

![Build Status](https://github.com/ArmandoSaboia/mlops-projects/workflows/CI/badge.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![GitHub](https://img.shields.io/github/license/ArmandoSaboia/mlops-projects.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/ArmandoSaboia/mlops-projects.svg)

## 🎯 Projects Overview

### Financial Services
1. [Fraud Detection](./projects/fraud_detection/) - Real-time transaction fraud detection
2. [Credit Risk](./projects/credit_risk/) - Credit risk assessment and scoring
3. [Market Analysis](./projects/market_analysis/) - Market trend prediction and analysis

### Healthcare
4. [Patient Outcomes](./projects/patient_outcomes/) - Patient outcome prediction
5. [Medical Imaging](./projects/medical_imaging/) - Disease detection from medical images
6. [Clinical Trials](./projects/clinical_trials/) - Clinical trial analysis and prediction

### Retail & E-commerce 
7. [Customer Segmentation](./projects/customer_segmentation/) - Customer behavior analysis
8. [Recommendation Engine](./projects/recommendation/) - Product recommendation system
9. [Inventory Management](./projects/inventory/) - Inventory optimization and forecasting

### Manufacturing
10. [Predictive Maintenance](./projects/predictive_maintenance/) - Equipment failure prediction
11. [Quality Control](./projects/quality_control/) - Manufacturing quality assurance
12. [Supply Chain](./projects/supply_chain/) - Supply chain optimization

### Marketing & Sales
13. [Lead Scoring](./projects/lead_scoring/) - Sales lead qualification
14. [Campaign Optimization](./projects/campaign_opt/) - Marketing campaign optimization
15. [Churn Prediction](./projects/churn/) - Customer churn prediction

### Natural Language Processing
16. [Sentiment Analysis](./projects/sentiment/) - Text sentiment classification
17. [Document Processing](./projects/document_processing/) - Automated document processing
18. [Chatbot](./projects/chatbot/) - Conversational AI assistant

## 🚀 Quick Start
### 1. Clone the Repository
```bash
git clone https://github.com/ArmandoSaboia/mlops-projects.git
cd mlops-projects
```
### 2. Choose a Project
#### Navigate to specific project directory
```bash
cd projects/<project_name>
```
#### Review project documentation
```bash
cat README.md
```
### 3. Set Up Environment
#### Create virtual environment
```bash
python -m venv venv
```
#### Activate virtual environment
```bash
source venv/bin/activate  # Linux/macOS
```
#### or
```bash
venv\Scripts\activate    # Windows
```
#### Install dependencies
```bash
pip install -r requirements.txt
```

## 🏗️ Repository Structure
```bash
mlops-projects/
├── projects/ 
├── common/ 
│ ├── monitoring/ 
│ ├── deployment/ 
│ └── testing/ 
├── docs/ 
├── scripts/ 
└── templates/
```

## 🛠️ Technology Stack

### Core Technologies
- **Languages**: Python 3.8+, SQL
- **ML Frameworks**: TensorFlow, PyTorch, scikit-learn
- **Data Processing**: Pandas, NumPy, Apache Spark
- **Data Warehouse**: Snowflake
- **Data Transformation**: dbt

### AI & ML Technologies
- **Machine Learning**: scikit-learn, XGBoost, LightGBM
- **Deep Learning**: TensorFlow, PyTorch
- **Generative AI**:
  - **LLMs**: LangChain, LlamaIndex
  - **Models**: GPT-4, Claude, Llama 2
  - **Vector DBs**: Pinecone, Weaviate, ChromaDB
  - **Embeddings**: OpenAI, Hugging Face
- **Computer Vision**: OpenCV, torchvision
- **NLP**: Transformers, spaCy, NLTK

### MLOps & Model Serving
- **Experiment Tracking**: MLflow
- **Pipeline Orchestration**: Airflow, Kubeflow
- **Feature Store**: Feast
- **Model Serving**: BentoML, TensorFlow Serving
- **API Development**: FastAPI
- **Model Registry**: MLflow Registry

### Visualization & UI
- **Data Visualization**: Plotly, Matplotlib
- **Dashboarding**: Streamlit, Grafana
- **Monitoring**: Prometheus

### Development & Testing
- **Data Validation**: Pydantic
- **Testing Data**: Faker
- **Version Control**: Git, DVC
- **CI/CD**: GitHub Actions

### Infrastructure & Deployment
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud Platforms**: 
  - AWS (SageMaker, EKS, S3, Bedrock)
  - GCP (Vertex AI, GKE, BigQuery)
  - Azure (Azure ML, AKS, OpenAI)

### Monitoring & Observability
- **Metrics**: Prometheus
- **Visualization**: Grafana
- **Logging**: ELK Stack
- **Tracing**: Jaeger

### Data Storage & Processing
- **Data Warehouse**: Snowflake
- **Data Lake**: Delta Lake
- **Stream Processing**: Apache Kafka
- **Batch Processing**: Apache Spark
- **Vector Stores**: Pinecone, Weaviate

### AI Development & Integration
- **LLM Frameworks**: LangChain, LlamaIndex
- **Model Hubs**: Hugging Face
- **Vector Databases**: Pinecone, Weaviate, ChromaDB
- **AI Services**: 
  - OpenAI API
  - Anthropic Claude
  - AWS Bedrock
  - Azure OpenAI

## 📚 Documentation

- [Getting Started Guide](./docs/getting_started.md)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Project Templates](./docs/templates.md)
- [Best Practices](./docs/best_practices.md)

## 🧪 Quality Assurance
```bash
Run tests
make test

Run linting
make lint

Run all checks
make check-all 
```

## 🔧 Support Channels
- [**Stack Overflow**](https://stackoverflow.com/questions/tagged/mlops)
- [**GitHub Discussions**](https://github.com/ArmandoSaboia/mlops-projects/discussions)
- [**Discord Community**](https://discord.gg/mlops)

## 🤝 Contributing
1. **Fork the Repository**
```bash
git clone https://github.com/ArmandoSaboia/mlops-projects.git
cd mlops-projects
```
2. **Create a Feature Branch**
```bash
git checkout -b feature/amazing-feature
```
3. **Make Your Changes**
```bash
git add .
git commit -m "Add amazing feature"
```
4. **Push to Branch**
```bash
git push origin feature/amazing-feature
```
5. **Open a Pull Request**
- [Visit Pull Requests](https://github.com/ArmandoSaboia/mlops-projects/pulls)
- **Click "New Pull Request"**
- **Select your branch**
- **Fill the template**


## 📈 Project Status

- **Production Ready**: 10 projects
- **Beta Testing**: 5 projects
- **Development**: 3 projects

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 📞 Support
- Create an [Issue](https://github.com/ArmandoSaboia/mlops-projects/issues)
- Create a [Discussion](https://github.com/ArmandoSaboia/mlops-projects/discussions)
- Email: 4rm4nd1nh0_br@protonmail.com

---

## 📧 Contact/Project Maintainer
- **Name: Armando Saboia**
- **Role: MLOps Engineer Enthusiast**
- **Location: Brazil 🇧🇷**
- **Email**: [4rm4nd1nh0_br@protonmail.com](mailto:4rm4nd1nh0_br@protonmail.com)
- **LinkedIn**: [Armando Saboia](https://www.linkedin.com/in/armandosaboia)

#### Experience
- **`2+ years experience`**
- **`MLOps enthusiast`**
- **`Open source contributor`**

## ⭐ Support the Project
#### If you find this repository useful, please consider:
  - **Giving it a star ⭐**
  - **Sharing with colleagues 🔄**
  - **Contributing to its development 🛠️**

<p align="center">
  Made with ❤️ by <a href="https://github.com/ArmandoSaboia">Armando Saboia</a>
</p>


