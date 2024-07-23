import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask(__name__)

# ログ設定
handler = RotatingFileHandler('/path/to/flask.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/')
def hello():
    app.logger.info('Hello, world!')
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
