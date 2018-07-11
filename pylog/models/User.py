from flask_login import UserMixin
from pylog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.CHAR(36))
    email = db.Column(db.VARCHAR(64), unique=True, index=True)
    user_name = db.Column(db.VARCHAR(20), nullable=False, index=True, unique=True)
    nick_name = db.Column(db.VARCHAR(20))
    avatar = db.Column(db.VARCHAR(150))
    password_hash = db.Column(db.CHAR(128), nullable=False)
    create_time = db.Column(db.TIMESTAMP)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def init_admin(user_name, password):
        data = {
            'user_name': user_name,
            'password': password,
            'guid': str(uuid.uuid1()),
            'nick_name': 'administrator',
            'create_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        user = User(**data)
        db.session.add(user)
        db.session.commit()


# callback function for flask-login extension
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
