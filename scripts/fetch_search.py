import requests
import json
import os
from datetime import date

API_KEY = os.getenv("RAINFOREST_API_KEY")

params = {
    "api_key": "",
    "type": "search",
    "amazon_domain": "amazon.com.br",
    "search_term": "notebook",
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

with open(f"{output_dir}/notebook.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Arquivo salvo com sucesso!")
