from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    user_name = StringField('用户名', validators=[DataRequired(), Length(4, 32)])
    password = PasswordField('密码', validators=[DataRequired()])
