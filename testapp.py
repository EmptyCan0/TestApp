from crypt import methods
from flask import Flask, render_template, request, redirect
import os

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# アップロードされたファイルを保存するディレクトリ
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 許可するファイル拡張子のリスト
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/')
def index():
    app.logger.info("upload開始")
    return render_template(
        'index.html'
    )


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'File {filename} uploaded successfully!'

@app.route('/upload',methods=['POST'])
def upload_file():
    print("start")
    app.logger.info("upload開始")
    if 'file' not in request.files:
        print("1")
        app.logger.error("ファイルがみつからない")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        print("2")
        app.logger.error("なまえが空")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        app.logger.info("ファイルのじょうほうOK ")
        filename = file.filename 
        print(filename)
        app.logger.info(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        app.logger.info("保存 ")
        return f'File {filename} uploaded successfully!'
    else:
        return 'Invalid file type.'

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)