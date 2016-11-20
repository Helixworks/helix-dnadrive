import os
from flask import Flask, request, redirect, url_for, send_from_directory,render_template
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect()
import magic
from dnadrive import dnadrive
mime = magic.Magic(mime=True)
UPLOAD_FOLDER = '/tmp/flaskfiles/'
WTF_CSRF_CHECK_DEFAULT = False
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/encode/", methods=['POST','PUT'])
@csrf.exempt
def encode():
    file = request.files['filedata']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    out_filename = filename.replace('.','_')+'.moss'
    out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
    gene = dnadrive.encode_file(file_path,out_file_path)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               out_filename, as_attachment=True)

@csrf.exempt
@app.route("/decode/", methods=['POST','PUT'])
def decode():
    file = request.files['filedata']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    out_filename = filename.replace('.moss','')
    out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
    gene = dnadrive.decode_file(file_path,out_file_path)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               out_filename, as_attachment=True)