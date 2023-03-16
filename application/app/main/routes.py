from app.main import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    """
    Route and method for rendering the index page.
    """
    return render_template('customer_facing/index.html', title='Index')
