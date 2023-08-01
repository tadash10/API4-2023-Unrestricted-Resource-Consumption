import requests

def make_api_request(url, headers=None, data=None):
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise APIRequestError(f"API request failed: {e}")

class APIRequestError(Exception):
    pass
