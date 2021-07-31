from models.category import Category
from middlewares.auth import auth_required
from flask import Blueprint, request, jsonify


category_blueprint = Blueprint('category', __name__)

@category_blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_all():
    categories = Category.get_all()
    data = []
    for category in categories:
        data.append(category.fields)
    return jsonify(data)

@category_blueprint.route('/<category_id>', methods=['GET'], strict_slashes=False)
def get_one(category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return jsonify({
            'error': 'CATEGORY_NOT_FOUND'
        })
    return jsonify(category.fields)

@category_blueprint.route('/', methods=['POST'], strict_slashes=False)
@auth_required
def create():
    params = request.get_json()
    category = Category(**params)
    category.save()
    return jsonify(category.fields)

@category_blueprint.route('/<category_id>', methods=['DELETE'])
@auth_required
def delete(category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return jsonify({
            'error': 'CATEGORY_NOT_FOUND'
        })
    category.delete()
    return jsonify({})

@category_blueprint.route('/<category_id>/increase', methods=['POST'], strict_slashes=False)
@auth_required
def increase(category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return jsonify({
            'error': 'CATEGORY_NOT_FOUND'
        })
    category.quantity_products = category.quantity_products + 1
    category.save()
    return jsonify(category.fields)

@category_blueprint.route('/<category_id>/decrease', methods=['POST'], strict_slashes=False)
@auth_required
def decrese(category_id):
    category = Category.get_by_id(category_id)
    if not category:
        return jsonify({
            'error': 'CATEGORY_NOT_FOUND'
        })
    if category.quantity_products > 0:
        category.quantity_products = category.quantity_products - 1
    category.save()
    return jsonify(category.fields)

@category_blueprint.route('/<category_id>', methods=['PUT'], strict_slashes=False)
@auth_required
def update(category_id):
    category = Category.get_by_id(category_id)

    if not category:
        return jsonify({
            'error': 'CATEGORY_NOT_FOUND'
        })

    params = request.get_json()

    if 'image_url' in params:
        category.image_url = params['image_url']
    if 'pretty_url' in params:
        category.pretty_url = params['pretty_url']
    if 'subtitle' in params:
        category.subtitle = params['subtitle']
    if 'title' in params:
        category.title = params['title']
    
    category.save()
    return jsonify(category.fields)