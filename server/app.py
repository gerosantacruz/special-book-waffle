from flask import Flask, jsonify
from flask_cors import CORS


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

@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status':'success',
        'books':BOOKS
    })

BOOKS = [
    {
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
    