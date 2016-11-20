import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import magic
from dnadrive import dnadrive
mime = magic.Magic(mime=True)
UPLOAD_FOLDER = '/tmp/flaskfiles/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/encode/", methods=['POST','PUT'])
def encode():
    file = request.files['filedata']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    out_filename = 'encoded_'+filename
    out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
    gene = dnadrive.encode_file(file_path,out_file_path)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               out_filename, as_attachment=True)

@app.route("/decode/", methods=['POST','PUT'])
def decode():
    file = request.files['filedata']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    out_filename = 'decoded_'+filename
    out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
    gene = dnadrive.decode_file(file_path,out_file_path)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               out_filename, as_attachment=True)