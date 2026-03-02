import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
r = requests.get(url, timeout=10)

print("Status:", r.status_code)
print("Content-Type:", r.headers.get("content-type"))
print("Body:", r.json())
