from crypt import methods
from flask import Blueprint, make_response, jsonify, request
posts_bp = Blueprint(
    "posts_bp", __name__,
)


@posts_bp.route('/posts', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'GET':
        res = make_response(jsonify({'hii': 'this is posts page'}))
        return res
    elif request.method == 'POST':
        details = request.args.to_dict()
        messages = details.get("messages")
        location = details.get("location")
        print(messages, location)
        res = make_response(
            jsonify({'message': messages, 'location': location}), 200)
        return res
