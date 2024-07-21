from crypt import methods
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# アップロードされたファイルを保存するディレクトリ
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 許可するファイル拡張子のリスト
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
	return render_template(
        'index.html'
    )

@app.route('/upload',methods=['POST'])
def upload_file():
    print("start")
    if 'file' not in request.files:
        print("1")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        print("2")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'File {filename} uploaded successfully!'
    else:
        return 'Invalid file type.'

if __name__ == "__main__":
	app.run(debug=True)