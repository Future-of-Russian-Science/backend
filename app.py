import os
from message import Error
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from mock import mock
from datetime import datetime

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def set_name(filename):
    format = filename.split(".")[1]
    return str(datetime.now())[:-7] + f'.{format}'

@app.route('/api/check', methods=['POST'])
@cross_origin()
def upload_file():
    queue = list(request.files)
    response = []

    if queue == 0:
        return jsonify(Error.IncorrectParameter)
    else:
        for photo in queue:
            file = request.files[photo]
            filename = secure_filename(set_name(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            response.append(mock(f'static/{filename}', photo[4:]))
    return jsonify(response)
