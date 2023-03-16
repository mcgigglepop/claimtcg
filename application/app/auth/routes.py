
from app.auth import bp
from flask import request, redirect, render_template, url_for, flash
from flask_login import current_user
from app import db
from app.models import User
import uuid

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
        
        # generate the userid hash
        userIdHashash = uuid.uuid4().hex

        # create a user object
        user = User(email=email, firstName=firstName, userIdHash=userIdHashash, lastName=lastName)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()

        # redirect to mfa
        return redirect(url_for('auth.mfa', ref=userIdHashash, register=True))
    
@bp.route('/mfa', methods=['GET', 'POST'])
def mfa():
    """
    Route and method for mfa. 
    User will redirect to dashboard if they are logged in
    or if the query parameter is not valid for a user.
    """
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))
        else:
            # get the user id hash from the url parameter
            userIdHash = request.args.get('ref')
            registerAttempt = request.args.get('register')

            # redirect if they try to force a fake user hash
            user = User.query.filter_by(userIdHash=userIdHash).first()
            if user is None:
                return redirect(url_for('auth.login'))
            
            # trigger the send mfa function 
            sendMfa(userIdHash)

            # sets the registration attempt value to true/false
            if registerAttempt is not None:
                registerAttempt = True
            else:
                registerAttempt = False

            return render_template('auth/mfa.html', register_attempt=registerAttempt, title='MFA')