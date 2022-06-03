# Overview

Leveraging GCP cloud functions, by using a [http trigger](https://cloud.google.com/functions/docs/writing/http) with a json payload to [add a new row](https://cloud.google.com/bigquery/streaming-data-into-bigquery#bigquery_table_insert_rows-python) to a bigquery table.

## Using

**TEST THE FUNCTION LOCALLY BEFORE DEPLOYMENT**, first create a python development environment inside your local machine with dependecies located in `requirements-dev.txt` using `python virtual environment`. After that make an `.env` file that contained your project, dataset, and table from bigquery, finally get your service account in the current directory to test the function with `pytest <function.py>`