from app.main import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    """
    Route and method for rendering the index page.
    """
    return render_template('customer_facing/index.html', title='Index')

@bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """
    Route and method for rendering the dashboard page.
    """
    return render_template('internal/dashboard.html', title='Dashboard')

@bp.route('/about', methods=['GET', 'POST'])
def about():
    """
    Route and method for rendering the about page.
    """
    return render_template('customer_facing/about.html', title='About Us')