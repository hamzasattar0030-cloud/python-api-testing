import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Test: Verify valid post returns correct data
def test_valid_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()

    if response.status_code == 200 and data["id"] == 1:
        print("[PASS] Valid post request")
    else:
         print("[FAIL] Valid post request")

# Test: Verify invalid post returns 404 or empty response
def test_invalid_post():
    response = requests.get(f"{BASE_URL}/posts/9999")

    if response.status_code == 404 or response.text == "{}":
        print("[PASS] Valid post request")
    else:
        print("[FAIL] Valid post request")

# Test: Verify user endpoint returns expected data fields
def test_user_data():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()

    if response.status_code == 200 and "email" in data:
        print("[PASS] Valid post request"))
    else:
        print("[FAIL] Valid post request")
        
# Test: Verify wrong endpoint returns 404 error
def test_wrong_endpoint():
    response = requests.get(f"{BASE_URL}/wrongendpoint")

    if response.status_code == 404:
       print("[PASS] Valid post request")
    else:
        print("[FAIL] Valid post request")

# Test: Verify correct user name is returned
def test_user_name():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()

    if response.status_code == 200 and data["name"] == "Leanne Graham":
        print("[PASS] Valid post request")
    else:
        print("[FAIL] Valid post request")

# Test: Verify posts endpoint returns a non-empty list
def test_posts_list():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()

    if response.status_code == 200 and isinstance(data, list) and len(data) > 0:
        print("[PASS] Valid post request")
    else:
        print("[FAIL] Valid post request")
        
        

def main():
    test_valid_post()
    test_invalid_post()
    test_user_data()
    test_wrong_endpoint()
    test_user_name()
    test_posts_list()

main()
