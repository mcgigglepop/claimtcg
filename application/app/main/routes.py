from app.main import bp
from flask import render_template, request
from flask_login import login_required, current_user
import json
from app import db
from app.models import Collection, Tag

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
    if request.method=='GET':
        
        collections_and_tags = db.session.query(Collection, Tag).join(Tag, Collection.id==Tag.collectionId).filter(Collection.user_id==current_user.id).all()

        # Print the results to check
        for c, t in collections_and_tags:
            print("Collection ID: ", c.id, "Collection Name: ", c.collectionName, "Tag: ", t.tagName)

        return render_template('internal/create-collection.html', title='Create Collection')
    else:
        collectionName = request.form.get('collectionName')
        visibilityType = request.form.get('visibilityType')
        collectionType = request.form.get('collectionType')

        collection = Collection(collectionName=collectionName, visibilityType=visibilityType, collectionType=collectionType, author=current_user)

        db.session.flush()
        tagObjects = []

        if request.form.get('tag'): tagObjects.append(Tag(tagName=request.form.get('tag'), collectionId=collection.id))
        if request.form.get('tagLine_0'): tagObjects.append(Tag(tagName=request.form.get('tagLine_0'), collectionId=collection.id))
        if request.form.get('tagLine_1'): tagObjects.append(Tag(tagName=request.form.get('tagLine_1'), collectionId=collection.id))
        if request.form.get('tagLine_2'): tagObjects.append(Tag(tagName=request.form.get('tagLine_2'), collectionId=collection.id))
        if request.form.get('tagLine_3'): tagObjects.append(Tag(tagName=request.form.get('tagLine_3'), collectionId=collection.id))
        if request.form.get('tagLine_4'): tagObjects.append(Tag(tagName=request.form.get('tagLine_4'), collectionId=collection.id))

        db.session.bulk_save_objects(tagObjects)
        db.session.commit()

        return render_template('internal/create-collection.html', title='Create Collection')