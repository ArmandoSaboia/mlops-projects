import mlflow
import xgboost as xgb
from sklearn.metrics import roc_auc_score
from typing import Dict, Tuple

class CreditRiskScorer:
    def __init__(self, config: Dict):
        self.config = config
        self.model = None
        
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """Train the credit risk scoring model."""
        mlflow.start_run()
        try:
            params = {
                'objective': 'binary:logistic',
                'max_depth': self.config['max_depth'],
                'learning_rate': self.config['learning_rate'],
                'n_estimators': self.config['n_estimators']
            }
            
            self.model = xgb.XGBClassifier(**params)
            self.model.fit(X_train, y_train)
            
            # Log metrics
            train_pred = self.model.predict_proba(X_train)[:, 1]
            mlflow.log_metric('train_auc', roc_auc_score(y_train, train_pred))
            
            # Log model
            mlflow.xgboost.log_model(self.model, "credit_risk_model")
            
        finally:
            mlflow.end_run() 