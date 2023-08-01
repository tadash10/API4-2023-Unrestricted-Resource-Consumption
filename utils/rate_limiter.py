import time

class TokenBucket:
    # ...

class APIRateLimiter:
    # ...

def configure_rate_limiter():
    return APIRateLimiter(
        capacity=config.RATE_LIMIT_CAPACITY,
        refill_rate=config.RATE_LIMIT_REFILL_RATE,
        max_requests_per_second=config.MAX_REQUESTS_PER_SECOND
    )
