from crypt import methods
from flask import Flask, render_template, request, redirect
import os

import logging

app = Flask(__name__)

# アップロードされたファイルを保存するディレクトリ
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 許可するファイル拡張子のリスト
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

@app.route('/')
def index():
	return render_template(
        'index.html'
    )

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
	app.run(debug=True)