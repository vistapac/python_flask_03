from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from extensions import db
from models.user import User


user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods = ['GET'])
@jwt_required()
def getUserInfo():
    #return jsonify({'error': 'User User User'}), 404
    # jwt_info = get_jwt()
    currentUserId = get_jwt_identity()
    user = User.query.get(currentUserId)
    
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    userInfo = {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'role': user.role
    }
    return jsonify(userInfo), 200

@user_bp.route('/users/<int:id>/role', methods = ['PUT'])
@jwt_required()
def changeUserRole(id):
    currentUserId = get_jwt_identity()
    currentUser = User.query.get(currentUserId)
    user = User.query.get(id)
    
    if not currentUser:
        return jsonify({'error': 'User not found'}), 404
    
    if currentUser.role != 'admin':
        return jsonify({'error': 'Unauthorized action. Only admin can change roles.'}), 403
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    newRole = data.get('role', 'user')
    
    user.role = newRole
    db.session.commit()
    
    return jsonify(message=f"User's role updated to {newRole} successfully."), 200
