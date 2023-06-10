from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from .forms import SignUpForm, LoginForm
from ..models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/login', methods=['GET', 'POST'])    
def loginPage():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password): 
                    flash(f'Logged In!' , 'success')
                    login_user(user)
                    return redirect(url_for('Home'))
                    
                else:
                    flash('Incorrect Username/Password', 'danger')
            else:
                flash('Incorrect Username/Password', 'danger')
            return redirect(url_for('auth.loginPage'))
    return render_template('login.html', form=form)



@auth.route('/register', methods=['GET', 'POST'])
@login_required
def registerPage():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            email = form.email.data
            number = form.number.data
            username = form.username.data
            password = form.password.data
            if User.query.filter_by(username=username).first():
                flash("That username already exists, please try another!", "warning")
                return redirect(url_for('auth.registerPage'))
            user = User(name, email, number, username, password)
            user.saveUser()
            flash(f"Welcome, {name.title()} has successfully been registered!", "success")
            return redirect(url_for('auth.loginPage'))                
    return render_template('register.html', form=form)

@auth.route('/logout')
def logOut():
    logout_user()
    flash("Logged out", "success")
    return redirect(url_for('Home'))