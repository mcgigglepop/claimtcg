
from app.auth import bp
from flask import request, redirect, render_template, url_for, flash, current_app
from flask_login import current_user, login_user, logout_user
from app import db
from app.models import User
import uuid
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendMfa(userIdHash):
    """
    Method to send MFA.
    Params: userIdHash: Hash to identify the user
    """
    # generate and set a current mfa token on the user record
    mfaToken = random.randint(1000,9999)
    userRecord = User.query.filter_by(userIdHash=userIdHash).first()
    userRecord.currentMfaCode = mfaToken
    db.session.commit()

    # get the user email to send the token to
    emailRecipient = userRecord.getEmail()
    htmlContent = "<p>Your MFA Code is {} </p>.".format(mfaToken)

    # check the environment and either print to log or send actual email
    if current_app.config['ENVIRONMENT'] == "local":
        print(emailRecipient)
        print(htmlContent)
    else:
        message = Mail(
            from_email=current_app.config['NO_REPLY_EMAIL'],
            to_emails=emailRecipient,
            subject="Your MFA Token",
            html_content=htmlContent)
        try:
            sg = SendGridAPIClient(current_app.config['SENDGRID_API_KEY'])
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
     

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
    else:
        # get front end data
        code1 = request.form.get('code1')
        code2 = request.form.get('code2')
        code3 = request.form.get('code3')
        code4 = request.form.get('code4')
        userIdHash = request.form.get('ref')
        registerAttempt = request.form.get('register-attempt')

        # append the codes together
        input_code = f'{code1}{code2}{code3}{code4}'

        # get the user object
        userObject = User.query.filter_by(userIdHash=userIdHash).first()

        # match the form mfa code input to the current mfa code stored on the user database record
        if str(input_code) == str(userObject.getCurrentMfaCode()):
            if registerAttempt == True:
                # verify the user
                userObject.isVerified = True
                db.session.commit()
            
            # log the user in and redirect to the dashboard
            login_user(userObject)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid Code. We sent you a new code.')
            # redirect to mfa sending userid hash as a url parameter
            return redirect(url_for('auth.mfa', register_attempt=registerAttempt, ref=userIdHash))
        
@bp.route('/logout')
def logout():
    """
    Log the user out of the platform
    """
    logout_user()
    return redirect(url_for('main.index'))