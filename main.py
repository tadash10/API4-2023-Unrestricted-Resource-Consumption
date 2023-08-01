import time
from utils import config, rate_limiter, logger, api_client, error_handling

def main():
    logger.initialize_logger()
    rate_limiter_obj = rate_limiter.configure_rate_limiter()

    for i in range(20):
        try:
            response = api_client.api_request_with_retry(config.API_BASE_URL, headers=config.API_HEADERS)
            print(f"API response: {response}")
        except error_handling.RateLimitExceededError as e:
            print(f"Rate limit exceeded: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except error_handling.APICallFailedError as e:
            print(f"API request failed: {e}")

if __name__ == "__main__":
    main()
