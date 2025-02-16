from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm  # เปลี่ยนการนำเข้าแบบสัมพัทธ์เป็นแบบสัมบูรณ์

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)
