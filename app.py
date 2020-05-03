from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '92bd8c9f9dd2b06bf27e644da0161cf7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'info')
        return redirect(url_for('home'))
    return render_template('register.html',  form=form)


@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'shuvo@gmail.com' and form.password.data == 'shuvo':
            flash(f'You have been logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Log in unsuccessfull. Enter a valid username and password', 'danger')

    return render_template('login.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
