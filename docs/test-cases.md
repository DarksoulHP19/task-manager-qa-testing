# ✅ Task Manager – QA Test Cases & Validation Summary

## 🔐 1. User Authentication

| Action                       | Input                                            | Expected Output                               | Actual Output                                                                 | Test Result |
|-----------------------------|--------------------------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------|-------------|
| Signup new user             | Name, Email, Password                            | Status: 201, User created                     | {"success": true, "message": "User registered successfully"}                  | ✅ PASS     |
| Signup with existing email  | Same email as above                              | Status: 400, Email exists                     | {"success": false, "message": "Email already exists"}                         | ✅ PASS     |
| Login with correct creds    | Valid Email/Password                             | Status: 200, JWT token                        | {"success": true, "token": "..."}                                             | ✅ PASS     |
| Login with wrong password   | Valid Email, wrong Password                      | Status: 401, Invalid credentials              | {"success": false, "message": "Invalid credentials"}                          | ✅ PASS     |

---

## 👥 2. Group Management

| Action               | Input                                                 | Expected Output                        | Actual Output                                                           | Test Result |
|----------------------|-------------------------------------------------------|----------------------------------------|------------------------------------------------------------------------|-------------|
| Create new group     | Group ID: G1, Title, Mentor, Members                  | Status: 201, Group created             | {"success": true, "message": "Group created successfully"}             | ✅ PASS     |
| Get mentor groups    | Mentor ID: Mentor1                                    | Status: 200, List of groups            | {"success": true, "data": [{"groupId": "G1", ...}]}                    | ✅ PASS     |
| Get group details    | Group ID: G1                                          | Status: 200, Group details             | {"success": true, "data": {"groupId": "G1", ...}}                       | ✅ PASS     |
| Update group         | Group ID: G1, New Title                               | Status: 200, Group updated             | {"success": true, "message": "Group updated successfully"}             | ✅ PASS     |

---

## ✅ 3. Error Cases

| Action                       | Input                                | Expected Output                      | Actual Output                                                                 | Test Result |
|-----------------------------|--------------------------------------|--------------------------------------|--------------------------------------------------------------------------------|-------------|
| Access without token        | None                                 | Status: 401, No token                | {"success": false, "message": "No token provided"}                            | ✅ PASS     |
| Access with invalid token   | Invalid JWT                          | Status: 401, Invalid token           | {"success": false, "message": "Invalid token"}                                | ✅ PASS     |
| Access coordinator as intern| Role: Intern on /manageUsers         | Status: 403, Access denied           | {"success": false, "message": "Access denied. Coordinator role required"}     | ✅ PASS     |

---

## 🔍 4. Data Validation

| Action                               | Input                                              | Expected Output                  | Actual Output                                                                  | Test Result |
|--------------------------------------|----------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------|-------------|
| Assign task with empty description   | Group ID: G1, description: ""                      | Status: 400, Description required| {"success": false, "message": "Task description is required"}                   | ✅ PASS     |
| Update user with invalid email       | Email: invalid-email                               | Status: 400, Invalid email       | {"success": false, "message": "Invalid email format"}                           | ✅ PASS     |
| Create group with missing field      | Group ID: G1, missing projectTitle                 | Status: 400, Required field      | {"success": false, "message": "Project title is required"}                      | ✅ PASS     |
| Complete non-existent task           | Task ID: T999                                      | Status: 404, Task not found      | {"success": false, "message": "Task not found"}                                 | ✅ PASS     |

---

## 📈 5. Progress Tracking Summary
| **Action**                         | **Input**                                 | **Expected Output**                        | **Actual Output**                                                                      | **Test Result** |
| ---------------------------------- | ----------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------- | --------------- |
| Assign task with empty description | Group ID: G1, Tasks: \[{description: ""}] | Status: 400, Error: Description required   | Status: 400, Response: `{"success": false, "message": "Task description is required"}` | ✅ PASS          |
| Update user with invalid email     | User ID: U1, Email: invalid-email         | Status: 400, Error: Invalid email          | Status: 400, Response: `{"success": false, "message": "Invalid email format"}`         | ✅ PASS          |
| Create group with missing field    | Group ID: G1 (missing projectTitle)       | Status: 400, Error: Required field missing | Status: 400, Response: `{"success": false, "message": "Project title is required"}`    | ✅ PASS          |
| Complete non-existent task         | Task ID: T999                             | Status: 404, Error: Task not found         | Status: 404, Response: `{"success": false, "message": "Task not found"}`               | ✅ PASS          |


