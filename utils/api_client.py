import requests
from .error_handling import APICallFailedError

def api_request_with_retry(url, headers=None, data=None, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries >= max_retries:
                raise APICallFailedError(f"API request failed after {max_retries} retries: {e}")
            # Sleep for a short duration before retrying
            time.sleep(1)

def handle_api_request(rate_limiter):
    if rate_limiter.allow_request():
        try:
            return api_request_with_retry(config.API_BASE_URL, headers=config.API_HEADERS)
        except APICallFailedError as e:
            print(f"API request failed: {e}")
    else:
        raise RateLimitExceededError("API rate limit exceeded. Please wait and try again later.")
