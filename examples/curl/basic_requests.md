# curl examples (beginner)

## 1) JSONPlaceholder success
curl -i https://jsonplaceholder.typicode.com/posts/1

## 2) JSONPlaceholder "missing" resource (practice not-found)
curl -i https://jsonplaceholder.typicode.com/posts/999999

## 3) GitHub API rate limit info
curl -i https://api.github.com/rate_limit

## 4) GitHub authenticated endpoint with a fake token (expect 401)
curl -i -H "Authorization: Bearer NOT_A_REAL_TOKEN" https://api.github.com/user
