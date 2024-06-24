from extensions import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), default='user')
    createdAt = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, email, password, username='username', role='user'):
        self.email = email
        #self.password = password
        self.set_password(password)  # 調用設置密碼的方法
        self.username = username
        self.role = role

    # @property   #   @property 將 password 方法變成一個屬性
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')    #防止直接讀取用戶的明文密碼，增強安全性。

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)