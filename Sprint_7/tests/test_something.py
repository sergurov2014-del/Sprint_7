import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
import data as D
import main
import helpers

BASE_URL = "https://qa-scooter.education-services.ru/api/v1"

payload = helpers.new_courier_data()
response = requests.post(f"{BASE_URL}/courier", json=payload)
id = requests.post(f"{BASE_URL}/courier/login", json=payload).json()
print(id['id'])
