import requests
import pandas as pd
import boto3
from io import StringIO
import os
import sys

# absolute path to vars
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
sys.path.append(parent_directory)
import vars

# fetch data
def fetch_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


# manipulate / transform the data
def process_data(data):
    df = pd.DataFrame(data)
    return df


# load the data
def save_data_to_csv(df, file_name):
    df.to_csv(f"step01_data_source/data/{file_name}", index=False)


# variables
bucket_name = vars.bucket_name
file_name = vars.file_name
data = fetch_data(vars.api_url)
processed_data = process_data(data)
save_data_to_csv(processed_data, file_name)
