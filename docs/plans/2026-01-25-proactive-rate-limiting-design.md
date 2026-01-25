# Proactive Rate Limiting Design

## Overview

Add opt-in rate limiting to prevent exceeding Flickr's 3600 queries/hour limit. This complements the existing reactive rate limit handling (HTTP 429 retry with backoff).

## Public API

```python
# Enable rate limiting (3600 requests/hour = ~1 request/second)
flickr_api.set_rate_limit(requests_per_hour=3600)

# Disable rate limiting
flickr_api.set_rate_limit(requests_per_hour=None)

# Get current setting
flickr_api.get_rate_limit()
# Returns: {"requests_per_hour": 3600} or {"requests_per_hour": None}

# Get status including last request time
flickr_api.get_rate_limit_status()
# Returns: {
#     "enabled": True,
#     "requests_per_hour": 3600,
#     "interval_seconds": 1.0,
#     "last_request_time": 1706198400.123  # or None if no requests yet
# }
```

## Design Decisions

1. **Simple sleep-based throttling** - Sleep a calculated interval between requests. Simple and predictable.

2. **Opt-in** - Disabled by default to preserve backward compatibility.

3. **Requests-per-hour configuration** - Maps directly to Flickr's documented limit (3600/hour). Internally converted to interval: `interval = 3600 / requests_per_hour`.

4. **Basic status API** - Provides enough info for debugging without over-engineering.

## Implementation

### Module Globals (method_call.py)

```python
_RATE_LIMIT_REQUESTS_PER_HOUR: float | None = None  # None = disabled
_RATE_LIMIT_LAST_REQUEST: float | None = None       # timestamp of last request
```

### Throttling Function

```python
def _maybe_wait_for_rate_limit() -> None:
    """Sleep if necessary to respect rate limit."""
    global _RATE_LIMIT_LAST_REQUEST

    if _RATE_LIMIT_REQUESTS_PER_HOUR is None:
        return  # Rate limiting disabled

    interval = 3600.0 / _RATE_LIMIT_REQUESTS_PER_HOUR

    if _RATE_LIMIT_LAST_REQUEST is not None:
        elapsed = time.time() - _RATE_LIMIT_LAST_REQUEST
        if elapsed < interval:
            time.sleep(interval - elapsed)

    _RATE_LIMIT_LAST_REQUEST = time.time()
```

### Integration Point

Called at the start of `_make_request_with_retry()`, before making each HTTP request.

## Files to Modify

- `flickr_api/method_call.py` - Add rate limit globals and functions, integrate into request flow
- `flickr_api/__init__.py` - Export new functions
- `test/test_rate_limit_throttle.py` - New test file

## Test Plan

1. `test_rate_limit_disabled_by_default` - Verify disabled initially
2. `test_set_and_get_rate_limit` - Set/get round-trip
3. `test_disable_rate_limit` - Set to None disables
4. `test_interval_calculation` - 3600 req/hour = 1.0s, 1800 = 2.0s
5. `test_get_rate_limit_status` - Status dict structure
6. `test_no_sleep_when_disabled` - No sleep when off
7. `test_sleeps_when_interval_not_elapsed` - Correct sleep duration
8. `test_no_sleep_when_interval_elapsed` - No sleep if enough time passed
9. `test_first_request_no_sleep` - First request doesn't wait
10. `test_updates_last_request_time` - Timestamp updates correctly

Tests will mock `time.sleep` and `time.time` for deterministic behavior.
