# Ticket: Authenticated endpoint fails with invalid token (401)

## User report (what they said)
- “I’m authenticated but the API says I’m not authorized.”

## Quick summary (one sentence)
- Calling an authenticated endpoint with an invalid token returns 401 Unauthorized.

## Environment
- API: GitHub API
- Endpoint: https://api.github.com/user
- Method: GET
- Timestamp/timezone: (add yours)
- Auth used: yes (Bearer token) — invalid on purpose

## Reproduction steps
1) Run:
   `curl -i -H "Authorization: Bearer NOT_A_REAL_TOKEN" https://api.github.com/user`
2) Observe status code and error message

## Expected vs actual
- Expected: success only with a valid token
- Actual: 401 Unauthorized

## Evidence
- Status code: 401
- Response body: (short snippet or description)

## Likely cause (best guess)
- Missing/invalid/expired token, or wrong auth method

## Next action
- Verify token validity + scopes; regenerate token if needed.
