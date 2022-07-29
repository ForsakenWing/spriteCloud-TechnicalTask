import logging
from pprint import pprint
from curlify import to_curl
import requests


def _validate_status_code(status_code):
    if status_code in range(200, 400):
        logging.info(f"OK, status_code={status_code}")
    elif status_code in range(400, 500):
        logging.warning(f"CLIENT ERROR, status_code={status_code}")
    elif status_code in range(500, 600):
        logging.critical(f"CRITICAL!, status_code={status_code}")


def post_request(url, data=None, json=None, **kwargs):
    print("========================================================")
    response = requests.post(url=url, data=data, json=json, **kwargs)
    _validate_status_code(response.status_code)
    print("======================= CURL ===========================")
    print(to_curl(response.request))
    print("======================= CURL ===========================")
    print("======================= REQUEST BODY =================-=")
    pprint(json)
    print("========================================================")
    print("====================== RESPONSE BODY ===================")
    pprint(response.json())
    print("========================================================")
    return response


def put_request(url, data=None, **kwargs):
    print("========================================================")
    response = requests.put(url=url, data=data, **kwargs)
    _validate_status_code(response.status_code)
    print("======================= CURL ==========================")
    print(to_curl(response.request))
    print("======================= CURL ==========================")
    pprint(response.json())
    print("========================================================")
    return response


def delete_request(url, **kwargs):
    print("========================================================")
    response = requests.delete(url=url, **kwargs)
    _validate_status_code(response.status_code)
    print("======================= CURL ==========================")
    print(to_curl(response.request))
    print("======================= CURL ==========================")
    pprint(response.json())
    print("========================================================")
    return response


def get_request(url, params=None, **kwargs):
    print("========================================================")
    response = requests.get(url=url, params=params, **kwargs)
    _validate_status_code(response.status_code)
    print("======================= CURL ==========================")
    print(to_curl(response.request))
    print("======================= CURL ==========================")
    pprint(response.json())
    print("========================================================")
    return response
