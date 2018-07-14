from . import auth
from pylog.models.User import User
from flask_login import login_user, login_required, logout_user
from flask import (
    render_template, redirect, request, url_for, flash
)

from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('登录成功！欢迎回来，%s' % user.user_name, 'success')
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('登录失败！用户名或密码错误,请重新登录', 'error')
    if form.errors:
        flash('登录失败，请尝试重新登录。', 'error')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('main.index'))


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/forget_password')
def forget_password():
    return render_template('auth/forget_password')
