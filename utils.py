import logging.config
import json
import os
from typing import Dict, Any

def setup_logging(default_config: Dict[str, Any]):
    """Sets up logging configuration."""
    config = default_config.get('logging', {})
    if 'level' in config:
        logging.basicConfig(level=config['level'],
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            handlers=[logging.StreamHandler()])
    else:
        logging.basicConfig(level=logging.INFO)

def load_config(config_file: str) -> Dict[str, Any]:
    """Loads a JSON configuration file."""
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")
    with open(config_file, 'r') as f:
        return json.load(f)
