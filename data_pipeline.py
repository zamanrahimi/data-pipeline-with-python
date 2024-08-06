# data_pipeline.py
import requests
import pandas as pd

def fetch_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    # Example processing: converting JSON to DataFrame
    df = pd.DataFrame(data)
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/users"
    FILE_PATH = "data.csv"

    data = fetch_data(API_URL)
    processed_data = process_data(data)
    save_data(processed_data, FILE_PATH)
