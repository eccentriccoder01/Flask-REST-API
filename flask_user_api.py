from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory storage for users
users = {}

# Helper function to validate user data
def validate_user_data(data, required_fields=['name', 'email']):
    if not data:
        return False, "No data provided"
    
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"
    
    # Basic email validation
    if 'email' in data and '@' not in data['email']:
        return False, "Invalid email format"
    
    return True, ""

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        'users': list(users.values()),
        'count': len(users)
    }), 200

# GET specific user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({'user': users[user_id]}), 200

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    
    # Validate input data
    is_valid, error_msg = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    # Check if email already exists
    for user in users.values():
        if user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 409
    
    # Create new user
    user_id = str(uuid.uuid4())
    new_user = {
        'id': user_id,
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age'),
        'phone': data.get('phone'),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    users[user_id] = new_user
    
    return jsonify({
        'message': 'User created successfully',
        'user': new_user
    }), 201

# PUT - Update existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.json
    
    # Validate input data
    is_valid, error_msg = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    # Check if email already exists (exclude current user)
    for uid, user in users.items():
        if uid != user_id and user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 409
    
    # Update user data
    users[user_id].update({
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age'),
        'phone': data.get('phone'),
        'updated_at': datetime.now().isoformat()
    })
    
    return jsonify({
        'message': 'User updated successfully',
        'user': users[user_id]
    }), 200

# DELETE user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    deleted_user = users.pop(user_id)
    
    return jsonify({
        'message': 'User deleted successfully',
        'deleted_user': deleted_user
    }), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_users': len(users)
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Method not allowed'}), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Add some sample data for testing
    sample_users = [
        {'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'phone': '+1234567890'},
        {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25, 'phone': '+0987654321'}
    ]
    
    for user_data in sample_users:
        user_id = str(uuid.uuid4())
        user_data.update({
            'id': user_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        })
        users[user_id] = user_data
    
    print(f"Starting Flask app with {len(users)} sample users")
    app.run(debug=True, host='0.0.0.0', port=5000)