from app.main import bp
from flask import render_template
from flask_login import login_required

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    """
    Route and method for rendering the index page.
    """
    return render_template('customer_facing/index.html', title='Index')

@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
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

@bp.route('/items', methods=['GET', 'POST'])
@login_required
def items():
    """
    Route and method for rendering the items page.
    """
    return render_template('internal/items.html', title='My Items')

@bp.route('/collections', methods=['GET', 'POST'])
@login_required
def collections():
    """
    Route and method for rendering the collections page.
    """
    return render_template('internal/collections.html', title='My Collections')

@bp.route('/create-collection', methods=['GET', 'POST'])
@login_required
def createCollection():
    """
    Route and method for rendering the create collection page.
    """
    return render_template('internal/create-collection.html', title='Create Collection')