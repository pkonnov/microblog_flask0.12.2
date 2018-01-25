from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Pavel'}
	posts = [
		{
			'autor': {'username': 'Loh'},
			'body': 'Ebat` kolotit`',
		},
		{
			'autor': {'username': 'Petya'},
			'body': 'Nu nihuya sebe'
		},
		{
			'autor': {'username': 'Vasya'},
			'body': 'Ebushki Vorobushki'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is none or not user.check_password(form.password.data):
			flash('Не валидные данные')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sing In', form=form)


app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
