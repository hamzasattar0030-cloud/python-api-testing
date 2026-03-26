import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Test 1: Valid post
response = requests.get(f"{BASE_URL}/posts/1")

print("Test 1: Valid post")
print("Status Code:", response.status_code)

data = response.json()

if response.status_code == 200 and data["id"] == 1:
    print("PASS\n")
else:
    print("FAIL\n")

# Test 2: Invalid post
response = requests.get(f"{BASE_URL}/posts/9999")

print("Test 2: Invalid post")
print("Status Code:", response.status_code)

if response.status_code == 404 or response.text == "{}":
    print("PASS\n")
else:
    print("FAIL\n")

# Test 3: Check user data
response = requests.get(f"{BASE_URL}/users/1")

print("Test 3: User data check")
print("Status Code:", response.status_code)

data = response.json()

if response.status_code == 200 and "email" in data:
    print("PASS\n")
else:
    print("FAIL\n")