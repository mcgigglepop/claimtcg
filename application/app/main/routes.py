from app.main import bp
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import func, select, text
import json
from app import db
from app.models import Collection, Tag, Item

from sqlalchemy.orm import aliased

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
    collections_and_tags = db.session.query(Collection, Tag, Item).outerjoin(Tag, Collection.id==Tag.collectionId).outerjoin(Item, Collection.id==Item.collectionId).filter(Collection.user_id==current_user.id).all()
    
    collectionsDictionary = {}

    for c, t, i in collections_and_tags:
        if c.id not in collectionsDictionary:
            collectionsDictionary[c.id] = {
                'collection_id': c.id,
                'collection_name': c.collectionName,
                'visibility_type': c.visibilityType,
                'collection_type': c.collectionType,
                'tags': [],
                'item_count': 0 if i is None else i
            }
        if t is not None:        
            collectionsDictionary[c.id]['tags'].append(t.tagName)

    return render_template('internal/collections.html', collections=list(collectionsDictionary.values()), title='My Collections')

@bp.route('/create-collection', methods=['GET', 'POST'])
@login_required
def createCollection():
    """
    Route and method for rendering the create collection page.
    """
    if request.method=='GET':
        return render_template('internal/create-collection.html', title='Create Collection')
    else:
        collectionName = request.form.get('collectionName')
        visibilityType = request.form.get('visibilityType')
        collectionType = request.form.get('collectionType')

        collection = Collection(collectionName=collectionName, visibilityType=visibilityType, collectionType=collectionType, author=current_user)
        
        db.session.add(collection)
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

        return redirect(url_for('main.collections'))