from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Don quijote de la mancha',
        'author': 'Cervantes',
        'read':True
    },
    {
        'title': 'La Iliada',
        'author': 'Homero',
        'read':True
    },
    {
        'title': 'El arte de la guerra',
        'author': 'Sun Tzu',
        'read':True
    }

]

if __name__ == '__main__':
    app.run()
    