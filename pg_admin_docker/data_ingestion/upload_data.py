import pandas as pd
from sqlalchemy import create_engine
from time import time
from datetime import datetime
import argparse
import os
import requests

def download_csv(url , file_name):
    response = requests.get(url)
    with open(file_name , "wb") as f:
        f.write(response.content)

def main(params):
    user = params.user
    password = params.password
    db = params.data_base
    table = params.table
    url = params.csv_file_api
    csv_name = "output.csv"


    download_csv(url , csv_name)
    
    df_iter = pd.read_csv(csv_name , iterator=True , chunksize=10000)
    df = next(df_iter)

    engine = create_engine(f"postgresql://{user}:{password}@db_pgadmin:5432/{db}")
    engine.connect()

    df.head(n=0).to_sql(table , con=engine , if_exists="replace")
    df.to_sql(table , con=engine , if_exists="append")
    start = datetime.now()
    print("start time",start)
    print("ingestion begin")
    try:
        while True:
            df = next(df_iter)
            df.to_sql(table , con=engine , if_exists="append")
    except StopIteration:
        print("ingestion complete")

    end = datetime.now()
    print("end time" , end)
    print("total time taken" , end - start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ingest data pipeline")

    parser.add_argument("--user" , help="add user for the postgres url")
    parser.add_argument("--password" , help="add password for the postgres url")
    parser.add_argument("--data_base" , help="enter the database name")
    parser.add_argument("--table" , help="enter the table name")
    parser.add_argument("--csv_file_api" , help="Enter the url of csv file")
    
    args = parser.parse_args()
    main(args)
    