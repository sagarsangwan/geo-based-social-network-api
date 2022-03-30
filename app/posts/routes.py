from crypt import methods
from flask import Blueprint, make_response, jsonify


# Blueprint Configuration

posts_bp = Blueprint(
    "posts_bp", __name__,
)


@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    res = make_response(jsonify({'hii': 'this is posts page'}))
    return res
