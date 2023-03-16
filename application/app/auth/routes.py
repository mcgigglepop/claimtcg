
from app.auth import bp
from flask import request, redirect, render_template, url_for, flash
from flask_login import current_user
from app import db
from app.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route and method for logging in a user account. 
    Will redirect to dashboard if they are logged in.
    """
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/login.html', title='Login')
        
@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route and method for registering a user account. 
    Will redirect to dashboard if they are logged in.
    """
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('auth/register.html', title='Register')
    else:
        # get the form data on submit
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

    # check if passwords match
        if password != confirmPassword: 
            flash('Passwords do not match')
            return redirect(url_for('auth.register'))
        
    # check if the email address exists already
        user = User.query.filter_by(email=email).first()
        if user is not None:
            flash('This email address already exists. Please use a different email address.')
            return redirect(url_for('auth.register'))