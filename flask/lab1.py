from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home',methods = ['GET'])
def first_func():
    print("First func run")
    return 'value returned by endpoint'

if __name__ == '__main__':
    app.run(debug=True)
