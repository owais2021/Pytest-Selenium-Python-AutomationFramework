import json

def load_config():
    with open('resources/test_config.json') as file:
        data = json.load(file)
    return data
CONFIG = load_config()
