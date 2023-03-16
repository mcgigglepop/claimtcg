
from app.auth import bp
from flask import request, redirect, render_template, url_for
from flask_login import current_user

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