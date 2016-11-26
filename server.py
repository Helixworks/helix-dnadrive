import os
from flask import Flask, request, redirect, url_for, send_from_directory,render_template,jsonify
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CsrfProtect
import hashlib
m = hashlib.md5()
csrf = CsrfProtect()
# import magic
from dnadrive import dnadrive
# mime = magic.Magic(mime=True)
UPLOAD_FOLDER = '/tmp/flaskfiles/'
WTF_CSRF_CHECK_DEFAULT = False
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/api/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/api/encode/", methods=['POST','PUT'])
@csrf.exempt
def encode():
    variant = int(request.form['variant'])
    if 'filedata' in request.files:
        file = request.files['filedata']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        out_filename = filename.replace('.','_')+'.moss'
        out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
        dnadrive.encode_file(file_path,out_file_path,variant)
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   out_filename, as_attachment=True)
    else:
        m.update(request.form['textdata'])
        filename =  m.hexdigest()[:5]
        filename = filename[:5]
        # print filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, "w") as text_file:
            text_file.write(request.form['textdata'])
        out_filename = filename.replace('.','_')+'.moss'
        out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
        dnadrive.encode_file(file_path,out_file_path,variant)
        with open(out_file_path, 'r') as myfile:
            data=myfile.read().replace('\n','</br>')
        return jsonify({"data":data})
    
@csrf.exempt
@app.route("/api/decode/", methods=['POST','PUT'])
def decode():
    if 'filedata' in request.files:
        file = request.files['filedata']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        infile = open(file_path, 'r')
        firstLine = infile.readline()
        # out_filename = "ds"
        out_filename = firstLine.split("|")[0].strip().split('@')[0]
        out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
        gene = dnadrive.decode_file(file_path,out_file_path)
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   out_filename, as_attachment=True)
    else:
        m.update(request.form['textdata'])
        filename =  m.hexdigest()[:5]
        filename = filename[:5]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, "w") as text_file:
            text_file.write(request.form['textdata'].replace('</br>','\n'))
        out_filename = filename.replace('.','_')+'.moss'
        out_file_path = os.path.join(app.config['UPLOAD_FOLDER'], out_filename)
        dnadrive.decode_file(file_path,out_file_path)
        with open(out_file_path, 'r') as myfile:
            data=myfile.read().replace('\n','</br>')
        return jsonify({"data":data})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)