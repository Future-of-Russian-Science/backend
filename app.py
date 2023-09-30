import os
from message import Error
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from mock import mock
from datetime import datetime

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def set_name(filename):
    format = filename.split(".")[1]
    return str(datetime.now())[:-7] + f'.{format}'

@app.route('/api/check', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(Error.IncorrectParameter)

    file = request.files['file']

    if file.filename == '':
        return jsonify(Error.FileNotUploaded)

    if file and allowed_file(file.filename):
        filename = secure_filename(set_name(file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(mock(file))

