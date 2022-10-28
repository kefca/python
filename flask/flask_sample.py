import os
from flask import Flask,url_for

#app = Flask(__name__, static_folder='.', static_url_path='')
app = Flask(__name__)

# ルーティング
@app.route("/hello")
def hello_world():
    return "Hello world!"

@app.route("/")
def index():
    #return app.send_static_file('index.html')
    return url_for("show_user_profile",username="ai_aacademy")

@app.route("/user/<username>")
def show_user_profile(username):
    return "UserName: " + str(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)

#app.run(port=8000, debug=True)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
