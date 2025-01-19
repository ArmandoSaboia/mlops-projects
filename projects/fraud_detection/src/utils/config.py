import yaml
from typing import Dict
import os

def load_config(config_path: str = None) -> Dict:
    """Load configuration from YAML file and environment variables."""
    if config_path is None:
        config_path = os.getenv('CONFIG_PATH', 'config/config.yaml')
    
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Override with environment variables
    env_vars = {
        'MODEL_PATH': 'model_path',
        'PREDICTION_THRESHOLD': 'threshold',
        'DATABASE_URL': 'database.url',
        'REDIS_URL': 'cache.url'
    }
    
    for env_var, config_key in env_vars.items():
        if os.getenv(env_var):
            _set_nested_config(config, config_key.split('.'), os.getenv(env_var))
    
    return config

def _set_nested_config(config: Dict, keys: list, value: str):
    """Set nested configuration value."""
    current = config
    for key in keys[:-1]:
        current = current.setdefault(key, {})
    current[keys[-1]] = value 