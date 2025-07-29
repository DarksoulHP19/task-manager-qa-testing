# Task Manager Backend API Testing

This directory contains comprehensive Postman collections and environment configurations for testing the Task Manager Backend API.

## Repository Analysis

The Task Manager Backend repository (https://github.com/DarksoulHP19/Task-Manager-Backend) has been analyzed and provides the following functionality:

### Architecture Overview
- **Framework**: Node.js with Express.js
- **Database**: MongoDB with Mongoose ODM
- **Authentication**: JWT-based authentication
- **Server Port**: 3000
- **Base API Path**: `/api/v1`

### Data Models
1. **User Model** (`model/User.js`)
   - Fields: fullName, email, password, userRole, tasksArr
   - Roles: "Coordinator", "Intern", "Mentor", "User"

2. **Group Model** (`model/Group.js`)
   - Fields: groupId, groupMentor, projectTitle, projectType, groupMembers
   - Project Types: cloud&devops, cybersecurity, dataScience, fullStack, java, python, react, webDevelopment

3. **Task Model** (`model/Task.js`)
   - Fields: groupId, groupMentor, groupMembers, tasks[]
   - Task Structure: description, is_completed

4. **Report Model** (`model/Report.js`)
   - Fields: groupId, file, isCorrect, remarks

### API Endpoints

#### User Management Routes (`/api/v1`)
- `POST /register` - User registration
- `POST /login` - User authentication
- `GET /getuser` - Get all users
- `POST /addRoles` - Add role to user (Coordinator required)
- `PUT /manageUsers/:id` - Update user details
- `DELETE /deleteUser/:id` - Delete user

#### Group Management Routes (`/api/v1`)
- `POST /addGroup` - Create new group (Coordinator required)
- `GET /getGroups` - Get all groups (Coordinator required)
- `GET /getMentorGroups` - Get groups for mentor (Mentor required)
- `GET /getMentorGroupDetails` - Get detailed group info (Mentor required)
- `PUT /updateGroup` - Update group (Coordinator required)
- `DELETE /deleteGroup/:groupId` - Delete group (Coordinator required)

#### Task Management Routes (`/api/v1`)
- `POST /assignTask` - Assign task to group (Mentor required)
- `GET /getTask` - Get tasks for user (Intern required)
- `POST /complteTask` - Complete task (Intern required)
- `POST /checkProgress` - Check group progress (Mentor required)

#### Health Check
- `GET /` - Server health check

## Files in this Directory

### `postman_collection.json`
Comprehensive Postman collection with 30+ test cases covering:

1. **User Management Tests**
   - User registration (valid/duplicate)
   - User login (valid/invalid credentials)
   - Role management
   - User updates

2. **Group Management Tests**
   - Group creation (valid/duplicate)
   - Group retrieval (all groups, mentor-specific)
   - Group updates and deletion
   - Permission-based access

3. **Task Management Tests**
   - Task assignment
   - Task retrieval
   - Task completion
   - Progress tracking

4. **Error Handling & Edge Cases**
   - Unauthorized access attempts
   - Invalid tokens
   - Missing required fields
   - Non-existent resources

5. **Server Health Checks**
   - Root endpoint validation

### `postman_enviornment.json`
Environment configuration with variables for:
- Base URLs and endpoints
- Test user credentials for different roles
- Dynamic variables for IDs and tokens
- Database and security configurations

## Role-Based Access Control

The API implements role-based access control with four user roles:

1. **User** - Default role for new registrations
2. **Intern** - Can view and complete assigned tasks
3. **Mentor** - Can assign tasks, view groups, check progress
4. **Coordinator** - Full access to user and group management

## Authentication Flow

1. Register a new user with `/register`
2. Login with credentials to get JWT token via `/login`
3. Use token in Authorization header as `Bearer <token>`
4. Assign appropriate roles via `/addRoles` (requires Coordinator role)

## Testing Workflow

### Prerequisites
1. Ensure the Task Manager Backend server is running on `http://localhost:3000`
2. MongoDB database is accessible
3. Postman is installed

### Setup Steps
1. Import `postman_collection.json` into Postman
2. Import `postman_enviornment.json` as environment
3. Select the "Task Manager Backend Environment" in Postman
4. Run the collection or individual test folders

### Recommended Test Sequence
1. **Server Health Check** - Verify server is running
2. **User Management** - Create users and assign roles
3. **Group Management** - Create and manage groups
4. **Task Management** - Assign and complete tasks
5. **Progress Tracking** - Monitor task completion
6. **Error Handling** - Test edge cases and security

## Test Data

The collection uses predefined test data that can be customized in the environment:
- Test users with different roles
- Sample groups and projects
- Task templates
- Error scenarios

## Expected Responses

### Success Responses
- Status: 200/201
- Format: `{ "success": true, "data": {...}, "message": "..." }`

### Error Responses
- Status: 400/401/404/500
- Format: `{ "success": false, "message": "...", "error": "..." }`

## Security Features Tested

1. **JWT Authentication** - Token validation
2. **Role-Based Access** - Permission enforcement
3. **Input Validation** - Required field checks
4. **Error Handling** - Proper error responses

## Database Schema Validation

The tests validate:
- User creation and authentication
- Group membership management
- Task assignment and completion tracking
- Progress calculation accuracy

## Notes

- Some endpoint names contain typos (e.g., `/complteTask` instead of `/completeTask`)
- The server uses different middleware files for different routes
- Password hashing is implemented with bcrypt
- MongoDB ObjectId references are used for relationships

## Troubleshooting

Common issues and solutions:
1. **401 Unauthorized** - Check if token is valid and user has required role
2. **404 Not Found** - Verify endpoint URLs and server is running
3. **400 Bad Request** - Check required fields in request body
4. **500 Server Error** - Check database connection and server logs
