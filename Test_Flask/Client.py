import requests
import json


def get_response():
    url = 'http://127.0.0.1:4000/'
    data = {
        "jsonrpc": "2.0",
        "method": "response_data",
        "params": {
            "name": "denis"
        }
    }
    response = requests.post(url, data=json.dumps(data))

    if response.status_code >= 500:
        return response.status_code, "I am dead"

    else:
        return response.status_code, "I am live"


if __name__ == "__main__":
    print("\n")
    print("################### Task_3 ########################")
    print(get_response())




