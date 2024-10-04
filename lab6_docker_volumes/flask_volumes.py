from flask import Flask, request

app = Flask(__name__)

# EndPoint with @ decorator
@app.route("/")
def hello_world():
    return  f'Hello World: Docker Volumes Lab. (available endpoint /ls to see local content)'

@app.route("/ls")
def list_files():
    file_content = open("/app/local_directory/message.txt").read()
    return file_content

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5003)