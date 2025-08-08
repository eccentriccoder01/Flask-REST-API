# Flask User Management REST API

A simple REST API built with Flask for managing user data. This API provides full CRUD (Create, Read, Update, Delete) operations for user management with in-memory storage.

## Features

- **GET** `/users` - Retrieve all users
- **GET** `/users/<id>` - Retrieve a specific user by ID
- **POST** `/users` - Create a new user
- **PUT** `/users/<id>` - Update an existing user
- **DELETE** `/users/<id>` - Delete a user
- **GET** `/health` - Health check endpoint

## Requirements

- Python 3.7+
- Flask

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd flask-user-api
```

2. Install required packages:
```bash
pip install flask
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. The API will be available at `http://localhost:5000`

## API Endpoints

### 1. Get All Users
- **URL**: `/users`
- **Method**: `GET`
- **Response**: List of all users with count

**Example Response:**
```json
{
  "users": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "name": "John Doe",
      "email": "john@example.com",
      "age": 30,
      "phone": "+1234567890",
      "created_at": "2025-01-01T10:00:00.000000",
      "updated_at": "2025-01-01T10:00:00.000000"
    }
  ],
  "count": 1
}
```

### 2. Get User by ID
- **URL**: `/users/<user_id>`
- **Method**: `GET`
- **Response**: Single user object

**Example Response:**
```json
{
  "user": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "phone": "+1234567890",
    "created_at": "2025-01-01T10:00:00.000000",
    "updated_at": "2025-01-01T10:00:00.000000"
  }
}
```

### 3. Create New User
- **URL**: `/users`
- **Method**: `POST`
- **Content-Type**: `application/json`

**Required Fields:**
- `name` (string)
- `email` (string)

**Optional Fields:**
- `age` (integer)
- `phone` (string)

**Example Request:**
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "age": 28,
  "phone": "+1122334455"
}
```

**Example Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": "456e7890-e89b-12d3-a456-426614174001",
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28,
    "phone": "+1122334455",
    "created_at": "2025-01-01T10:30:00.000000",
    "updated_at": "2025-01-01T10:30:00.000000"
  }
}
```

### 4. Update User
- **URL**: `/users/<user_id>`
- **Method**: `PUT`
- **Content-Type**: `application/json`

**Example Request:**
```json
{
  "name": "Alice Smith",
  "email": "alice.smith@example.com",
  "age": 29
}
```

### 5. Delete User
- **URL**: `/users/<user_id>`
- **Method**: `DELETE`

**Example Response:**
```json
{
  "message": "User deleted successfully",
  "deleted_user": {
    "id": "456e7890-e89b-12d3-a456-426614174001",
    "name": "Alice Smith",
    "email": "alice.smith@example.com"
  }
}
```

### 6. Health Check
- **URL**: `/health`
- **Method**: `GET`

**Example Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-01T10:00:00.000000",
  "total_users": 2
}
```

## Testing with cURL

### Get all users:
```bash
curl -X GET http://localhost:5000/users
```

### Get specific user:
```bash
curl -X GET http://localhost:5000/users/<user_id>
```

### Create new user:
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","age":25}'
```

### Update user:
```bash
curl -X PUT http://localhost:5000/users/<user_id> \
  -H "Content-Type: application/json" \
  -d '{"name":"Updated Name","email":"updated@example.com"}'
```

### Delete user:
```bash
curl -X DELETE http://localhost:5000/users/<user_id>
```

## Testing with Postman

1. Import the following requests into Postman:
2. Set the base URL to `http://localhost:5000`
3. For POST and PUT requests, set Content-Type header to `application/json`
4. Use the JSON examples provided above in the request body

## Error Handling

The API returns appropriate HTTP status codes:

- **200** - Success
- **201** - Created
- **400** - Bad Request (validation errors)
- **404** - Not Found
- **405** - Method Not Allowed
- **409** - Conflict (duplicate email)
- **500** - Internal Server Error

## Data Storage

This API uses in-memory storage (Python dictionary), which means:
- Data is lost when the server restarts
- Suitable for development and testing
- Can be easily replaced with a database (SQLite, PostgreSQL, etc.)

## Sample Data

The application starts with 2 sample users for testing purposes.

## Future Enhancements

- Add database integration (SQLite/PostgreSQL)
- Implement user authentication
- Add input validation for phone numbers
- Implement pagination for large datasets
- Add logging
- Add unit tests

## Author

Created as part of Python Developer Internship - Task 4