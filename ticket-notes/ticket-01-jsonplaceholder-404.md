# Ticket: JSONPlaceholder returns not found / empty response for missing resource

## User report (what they said)
- “I’m trying to fetch a post but it doesn’t work.”

## Quick summary (one sentence)
- Requesting a post id that doesn’t exist returns not found/empty behavior.

## Environment
- API: JSONPlaceholder
- Endpoint: https://jsonplaceholder.typicode.com/posts/999999
- Method: GET
- Timestamp/timezone: (add your time, e.g., 2026-03-02 20:45 Dublin)
- Auth used: no (public API)

## Reproduction steps
1) Run: `curl -i https://jsonplaceholder.typicode.com/posts/999999`
2) Observe response

## Expected vs actual
- Expected: 404 Not Found or clear "not found" message
- Actual: (write what you saw)

## Evidence
- Status code: (e.g., 404 or 200)
- Response body: (short snippet or description)

## Likely cause (best guess)
- Requested resource id does not exist

## Next action
- Confirm correct id; improve messaging if this were a real product.
