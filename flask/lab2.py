from flask import Flask, request

app = Flask(__name__)

@app.route("/getname", methods = ['GET', 'POST'])
def get_name():
    data = request.get_json()
    user_entered_name = str(data['name'])
    return user_entered_name

@app.route("/getModulus", methods = ["GET", 'post'])
# can call with http://127.0.0.1:5000/getModulus?num1=10&num2=20 too
def get_mean():
    number_1 = int(request.args.get("num1"))
    number_2 = int(request.args.get("num2"))
    return str(number_1 % number_2 )

@app.route("/getmin", methods = ['GET'])
# can call with http://127.0.0.1:5000/getmin?num1=10&num2=20 too
def get_max():
    data = request.get_json()
    number_1 = int(data['num1'])
    number_2 = int(data['num2'])
    return str(min(number_1, number_2))
    
if __name__== "__main__":
    app.run(debug=True)

# RUNNING THE APP: python -m flask --app flask/quickstart.py run
