import yaml
import os


# Function to load the configuration from config.yaml
def load_config():
    # Get the path of config.yaml file relative to this file's location
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')

    # Open and read the YAML file
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)  # Parse YAML content into a Python dictionary

    return config