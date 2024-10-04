from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# EndPoint with @ decorator
@app.route("/first")
def hello_world2():
    return "<p>/first path</p>"


if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000)
