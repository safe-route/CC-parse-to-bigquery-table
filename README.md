# Overview

Leveraging GCP cloud functions, by using a [http trigger](https://cloud.google.com/functions/docs/writing/http) with a json payload to [add a new row](https://cloud.google.com/bigquery/streaming-data-into-bigquery#bigquery_table_insert_rows-python) to a bigquery table.


## Summary

This functions purpose was meant to be a rudimentary pipeline builder to send an info via android app to run a series of job to update the **clustering.json** we used as a basis for geofence in the Safe Route Android app, triggered via http request.

## Reference

Basic google docs in legacy bigquery api and http trigger function referred in title, [http trigger](https://cloud.google.com/functions/docs/writing/http) with a json payload to [add a new row](https://cloud.google.com/bigquery/streaming-data-into-bigquery#bigquery_table_insert_rows-python) to a bigquery table.

Other than that basic unit test is also provided [here](https://cloud.google.com/functions/docs/samples/functions-http-unit-test). Environment setup is following Google's recommendation of building cloud functions development environment [here](https://cloud.google.com/functions/docs/running/overview), and by following the code examples [here](https://cloud.google.com/functions/docs/calling/http#functions-calling-http-nodejs), to act as a basis for the code development environment.

The development environment of this function is initiated by using project wide python's [virtual environment](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.), and usage of [pip](https://pypi.org/project/pip/).

## Structure

There are no structure in this repository, you can add anything on the root of the repository without any repercussions.

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

Check your bigquery table to observe the change
