import json
from pathlib import Path

test_login_data_path = Path(__file__).parent.parent / 'test_data' / 'login_data.json'
with open(test_login_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]
    
test_login_failed_data_path = Path(__file__).parent.parent / 'test_data' / 'login_failed.json'
with open(test_login_failed_data_path) as file:
    test_data_2 = json.load(file)
    test_list_2 = test_data_2["data"]
