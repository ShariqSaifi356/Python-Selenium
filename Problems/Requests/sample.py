import requests as req  # type: ignore

BASE_URL = "https://dummyjson.com"

# Valid endpoint with a path
response = req.get(f"{BASE_URL}/users/1")
print("Status code:", response.status_code)
print("URL:", response.url)

try:
    print("JSON:", response.json())
except ValueError as e:
    print("This response is not valid JSON:", e)
    print("Response text:", response.text[:200])

# Correct way to use query parameters
response = req.get(f"{BASE_URL}/users/1", params={"limit": 2})
print("Status code:", response.status_code)
print("URL:", response.url)
print("JSON:", response.json())