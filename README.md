# Overview

Leveraging GCP cloud functions, by using a [http trigger](https://cloud.google.com/functions/docs/writing/http) with a json payload to [add a new row](https://cloud.google.com/bigquery/streaming-data-into-bigquery#bigquery_table_insert_rows-python) to a bigquery table.

## Using

**TEST THE FUNCTION LOCALLY BEFORE DEPLOYMENT**, first create a python development environment inside your local machine with dependecies located in `requirements-dev.txt` using `python virtual environment`. After that make an `.env` file that contained your project, dataset, and table from bigquery, finally get your service account in the current directory to test the function with `pytest <function.py>`

```bash
curl -m 70 -X POST https://asia-southeast2-safe-route-351803.cloudfunctions.net/add-row-jakarta_crime_history \
-H "Authorization:bearer $(gcloud auth print-identity-token)" \
-H "Content-Type:application/json" \
-d '{
    "date": "2022-01-02",
    "time": 15,
    "latitude": -6.12597108,
    "longitude": 106.9203174
}'
```

Should return

```bash
"Insert success"
```
