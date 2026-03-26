# API Test Cases

## TC001 - Verify valid post request returns success
**Endpoint:** /posts/1  
**Method:** GET  

**Steps:**
1. Send GET request to /posts/1

**Expected Result:**
- Status code is 200
- Response contains id = 1

---

## TC002 - Verify invalid post request returns not found
**Endpoint:** /posts/9999  
**Method:** GET  

**Steps:**
1. Send GET request to /posts/9999

**Expected Result:**
- Status code is 404 or empty response

---

## TC003 - Verify valid user request returns user data
**Endpoint:** /users/1  
**Method:** GET  

**Steps:**
1. Send GET request to /users/1

**Expected Result:**
- Status code is 200
- Response contains an email field

---

## TC007 - Verify posts list is returned
**Endpoint:** /posts  
**Method:** GET  

**Steps:**
1. Send GET request to /posts  

**Expected Result:**
- Status code is 200  
- Response is a list  
- List contains at least one item  