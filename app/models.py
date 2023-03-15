from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app
from itsdangerous import TimedSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def _repr_(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], 'confirmation')
        return s.dumps(self.id)

    def confirm(self, token, max_age=3600):
        s = Serializer(current_app.config['SECRET_KEY'], 'confirmation')
        try:
            data = s.loads(token, max_age=max_age)
        except:
            return False
        if data != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], 'reset')
        return s.dumps(self.id)

    @staticmethod
    def reset_password(token, new_password, max_age=3600):
        s = Serializer(current_app.config['SECRET_KEY'], 'reset')
        try:
            user_id = s.loads(token, max_age=max_age)
            #import pdb;pdb.set_trace()
        except:
            return False
        #user_id = data.get(str('reset'))
        user = User.query.get(user_id)
        db.session.add(user)
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True


    def _repr_(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))