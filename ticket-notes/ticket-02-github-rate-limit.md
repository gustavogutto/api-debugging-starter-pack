# Ticket: GitHub API rate limit headers show remaining quota

## User report (what they said)
- “My API calls started failing after a while.”

## Quick summary (one sentence)
- GitHub API exposes rate limit information via response headers and JSON.

## Environment
- API: GitHub API (public)
- Endpoint: https://api.github.com/rate_limit
- Method: GET
- Timestamp/timezone: (add yours)
- Auth used: no (unauthenticated)

## Reproduction steps
1) Run: `curl -i https://api.github.com/rate_limit`
2) Look for rate limit headers

## Expected vs actual
- Expected: a JSON response describing limits
- Actual: response includes remaining quota + reset time

## Evidence
- Status code: (likely 200)
- Key headers to note:
  - X-RateLimit-Limit:
  - X-RateLimit-Remaining:
  - X-RateLimit-Reset:

## Likely cause (best guess)
- Unauthenticated requests have low quota; heavy usage can hit limits.

## Next action
- Recommend retries/backoff, caching, and authenticated requests if appropriate.
