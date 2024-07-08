from flask import Flask, jsonify, request
from flask.typing import ResponseReturnValue
from flask_cors import CORS

from .types.interface import TestMessage

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong() -> ResponseReturnValue:
    """Sanity check route to ensure the backend is functional."""
    return jsonify('pong!')


@app.route('/object_test', methods=['GET', 'POST'])
def object_test() -> ResponseReturnValue:
    if request.method == 'POST':
        post_data = TestMessage(**request.get_json())
        print(post_data)

    return jsonify(TestMessage(name='testing_55', age=34.5))


if __name__ == '__main__':
    app.run()
