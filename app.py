from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my web app"

@app.route("/math", methods=["GET"])
def math_operation():
    operation = request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]
    
    if operation=="addition":
        result = int(number1) + int(number2)
    elif operation=="multiply":
        result = int(number1)*int(number2)
    elif operation=="division":
        result= int(number1)/int(number2)
    else:
        result= int(number1)-int(number2)
    return "The result of the {} operation is {}".format(operation, result)

print(__name__)

if __name__ == "__main__":
    app.run(debug=True)