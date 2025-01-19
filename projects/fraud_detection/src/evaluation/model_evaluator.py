import numpy as np
import pandas as pd
from sklearn.metrics import (
    roc_auc_score,
    precision_recall_curve,
    average_precision_score,
    confusion_matrix
)
from typing import Dict, Tuple
import matplotlib.pyplot as plt
import seaborn as sns

class ModelEvaluator:
    def __init__(self, config: Dict):
        self.config = config
        self.metrics = {}
    
    def evaluate_model(self, y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray) -> Dict:
        """Comprehensive model evaluation."""
        self.metrics = {
            'roc_auc': roc_auc_score(y_true, y_prob),
            'avg_precision': average_precision_score(y_true, y_prob),
            'confusion_matrix': confusion_matrix(y_true, y_pred).tolist()
        }
        
        # Calculate precision-recall curve
        precision, recall, thresholds = precision_recall_curve(y_true, y_prob)
        self.metrics['precision_recall'] = {
            'precision': precision.tolist(),
            'recall': recall.tolist(),
            'thresholds': thresholds.tolist()
        }
        
        return self.metrics
    
    def plot_confusion_matrix(self, save_path: str = None):
        """Plot confusion matrix heatmap."""
        cm = np.array(self.metrics['confusion_matrix'])
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            xticklabels=['Not Fraud', 'Fraud'],
            yticklabels=['Not Fraud', 'Fraud']
        )
        plt.title('Confusion Matrix')
        if save_path:
            plt.savefig(save_path)
        plt.close()
    
    def find_optimal_threshold(self, y_true: np.ndarray, y_prob: np.ndarray) -> float:
        """Find optimal classification threshold using F1 score."""
        precision, recall, thresholds = precision_recall_curve(y_true, y_prob)
        f1_scores = 2 * (precision * recall) / (precision + recall + 1e-7)
        optimal_threshold = thresholds[np.argmax(f1_scores)]
        return optimal_threshold 