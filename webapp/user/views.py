from flask import Blueprint, Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp import db


blueprint = Blueprint('user', __name__, url_prefix='/users', template_folder='templates')


@blueprint.route('/login')
def login():
    #Блок исключающий повторнную авторизацию для уже авторизированных пользователей
    if current_user.is_authenticated:
        #заменить user.login на адрес главной страницы сайта
        return redirect(url_for('user.login'))

    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form = login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            #заменить user.login на адрес главной страницы сайта
            return redirect(url_for('user.login'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))   


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из сессии')
    #заменить user.login на адрес главной страницы сайта
    return redirect(url_for('user.login'))

@blueprint.route('/register')
def register():
    #Блок исключающий повторнную авторизацию для уже авторизированных пользователей
    if current_user.is_authenticated:
        #заменить user.login на адрес главной страницы сайта
        return redirect(url_for('user.login'))

    title = "Регистрация"
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form = form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role=form.roles.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))   