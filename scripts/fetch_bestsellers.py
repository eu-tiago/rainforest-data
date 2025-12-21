import requests
import json
import os
from datetime import date

API_KEY = os.getenv("RAINFOREST_API_KEY")

params = {
    "api_key": API_KEY,
    "type": "bestsellers",
    "amazon_domain": "amazon.com.br",
    "category_id": "bestsellers_appliances",
    "page": "1",
    "max_page": "5",
    "output": "json"
}

response = requests.get(
    "https://api.rainforestapi.com/request",
    params=params
)

data = response.json()

today = date.today().isoformat()
output_dir = f"data/{today}"
os.makedirs(output_dir, exist_ok=True)

file_path = f"{output_dir}/bestsellers_appliances.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Bestsellers salvos com sucesso!")
