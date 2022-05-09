# coding: UTF-8
# インストールした「flask.py」から「Flask」Classをimport
from flask import Flask

# Flaskクラスをnewしてappに代入
app = Flask(__name__)


# urlとして”/hello”がgetメソッドで呼ばれると定義した関数が実行される
@ app.route('/hello')
def hello():
    hello = "Hello world"
    return hello


@ app.route('/')
def main():
    hello = "Hello world"
    return hello


if __name__ == "__main__":
    # runメソッドでビルトインサーバーが走る
    app.run()
