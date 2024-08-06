import requests
import pandas as pd
import boto3
from io import StringIO

def fetch_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    df = pd.DataFrame(data)
    return df

def save_data_to_s3(df, bucket_name, file_name):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/users"
    BUCKET_NAME = "github-data-storage"
    FILE_NAME = "data.csv"

    data = fetch_data(API_URL)
    processed_data = process_data(data)
    save_data_to_s3(processed_data, BUCKET_NAME, FILE_NAME)
