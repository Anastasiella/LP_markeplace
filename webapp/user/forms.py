from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email, EqualTo




class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    my_choices = [('1', 'Покупатель'), ('2', 'Продавец')]
    roles = SelectMultipleField('Выбирите вашу роль', choices = my_choices, default = ['1', '3'])
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})




class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField()
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})



