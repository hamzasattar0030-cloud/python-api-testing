import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_valid_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()

    if response.status_code == 200 and data["id"] == 1:
        print("Test valid post: PASS")
    else:
        print("Test valid post: FAIL")

def test_invalid_post():
    response = requests.get(f"{BASE_URL}/posts/9999")

    if response.status_code == 404 or response.text == "{}":
        print("Test invalid post: PASS")
    else:
        print("Test invalid post: FAIL")

def test_user_data():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()

    if response.status_code == 200 and "email" in data:
        print("Test user data: PASS")
    else:
        print("Test user data: FAIL")

def main():
    test_valid_post()
    test_invalid_post()
    test_user_data()

main()