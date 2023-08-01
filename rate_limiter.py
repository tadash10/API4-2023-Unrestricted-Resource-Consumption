import time
import threading

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def _refill_tokens(self):
        now = time.time()
        time_since_last_refill = now - self.last_refill_time
        new_tokens = time_since_last_refill * self.refill_rate
        with self.lock:
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_refill_time = now

    def consume(self, tokens):
        with self.lock:
            if tokens <= self.tokens:
                self.tokens -= tokens
                return True
            return False

class APIRateLimiter:
    def __init__(self, capacity, refill_rate, max_requests_per_second):
        self.token_bucket = TokenBucket(capacity, refill_rate)
        self.max_requests_per_second = max_requests_per_second

    def allow_request(self):
        self.token_bucket._refill_tokens()
        return self.token_bucket.consume(self.max_requests_per_second)
