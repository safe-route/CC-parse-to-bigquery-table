import os

from flask import escape
from google.cloud import bigquery
from os.path import join, dirname
from google.cloud import bigquery
from http import client
from dotenv import load_dotenv
import functions_framework

client = bigquery.Client.from_service_account_json('./secret.json')

@functions_framework.http
def insert_to_row(request):
    """
    Insert payload to bigquery table as row.
    """
    
    content_type = request.headers['content-type']

    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
    else:
        raise ValueError("JSON is invalid")
    row_to_insert = [request_json]

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    client = bigquery.Client()
    table_id = str(os.environ.get("PROJECT") + "." + os.environ.get("DATASET") + "."+ os.environ.get("TABLE"))
    print(table_id)

    errors = client.insert_rows_json(
        table_id, row_to_insert, row_ids=[None] * len(row_to_insert)
    )
    if errors == []:
        print(f'''New row added to {os.environ.get("TABLE")}.''')
    else:
        print("Something bad happened when inserting row.")

    print("Insert Success!")