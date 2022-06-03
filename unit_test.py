from unittest.mock import MagicMock
from unittest.mock import MagicMock
from datetime import datetime

import main


cur_date = datetime.today().strftime('%Y-%m-%d')
cur_hour = datetime.today().strftime('%H')

def test_print_name():
    headers = {'content-type': 'application/json'}
    data = {
        "date": cur_date,
        "time": cur_hour,
        "latitude": -6.12597108,
        "longitude": 106.9203174
    }
    req = MagicMock(get_json=MagicMock(return_value=data), args=data, headers=headers)

    # Call tested function
    assert main.insert_to_row(req) == "Insert success!"


def test_print_insert_to_row():
    data = {}
    req = MagicMock(get_json=MagicMock(return_value=data), args=data)

    # Call tested function
    assert main.insert_to_row(req) == "Insert success"