# main.py
from dotenv import load_dotenv
import requests
import json
import os
import time

def fetch_data():
    load_dotenv("creds.env")

    API_KEY = os.getenv("API_KEY")
    url = "https://reqres.in/api/users?page=2"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        ids = [user["id"] for user in data["data"]]
        print("IDs:", ids)
        print("Number of IDs:", len(ids))
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    while True:
        fetch_data()
        time.sleep(10)
