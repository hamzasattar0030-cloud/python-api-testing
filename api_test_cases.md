# API Test Cases

## TC001 - Verify valid post request
**Endpoint:** /posts/1  
**Method:** GET

**Steps:**
1. Send GET request to /posts/1

**Expected Result:**
- Status code is 200
- Response contains id = 1

---

## TC002 - Verify invalid post request
**Endpoint:** /posts/9999  
**Method:** GET

**Steps:**
1. Send GET request to /posts/9999

**Expected Result:**
- Status code is 404 or empty response

---

## TC003 - Verify valid user data response
**Endpoint:** /users/1  
**Method:** GET

**Steps:**
1. Send GET request to /users/1

**Expected Result:**
- Status code is 200
- Response contains an email field

---

## TC004 - Verify response structure
**Endpoint:** /users/1  
**Method:** GET

**Steps:**
1. Send GET request to /users/1

**Expected Result:**
- Response contains expected fields such as id, name, and email
