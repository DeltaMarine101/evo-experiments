from flask import Flask, jsonify
from flask.typing import ResponseReturnValue
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong() -> ResponseReturnValue:
    """Sanity check route to ensure the backend is functional."""
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
