#允許將應用程式的不同部分分解成模塊
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
#創建新的 JWT（JSON Web Token）訪問令牌 #應用於路由時，該路由需要有效的 JWT 訪問令牌才能被訪問  #從 JWT 中獲取當前用戶的身份
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db
from models.user import User


#auth這個名稱在 Flask 應用程式內部用於識別這個 Blueprint。
auth_bp = Blueprint('auth', __name__)   

@auth_bp.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    username = data.get('username', 'username')
    role = data.get('role', 'user')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    existingUser = User.query.filter_by(email=email).first()
    if existingUser:
        return jsonify({'error': 'User already exists'}), 400

    newUser = User(email = email, password = password, username = username, role = role)
    db.session.add(newUser)
    db.session.commit()

    response_data = {
        'message': 'User registered successfully',
        'data': {
            'email': newUser.email,
            'username': newUser.username,
            'role': newUser.role,
            'id': newUser.id            
        }
    }
    return jsonify(response_data), 201

@auth_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email = email).first()

    if not user:
        return jsonify({'error': 'Email not found'}), 401
    
    if check_password_hash(user.password_hash, data['password']):
        return jsonify({'error': 'Incorrect password'}), 401
    
    # 如果用戶存在且密碼正確，生成 JWT Token
    jwtToken = create_access_token(identity = user.id)

    response_data = {
        'message': 'Login successful',
        'data': {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'role': user.role,
            'token': jwtToken
        }
    }
    return jsonify(response_data), 200