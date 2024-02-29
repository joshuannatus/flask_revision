from flask import Flask, render_template, request

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
        result = number1+number2
    elif operation=="multiply":
        result = number1*number2
    elif operation=="division":
        result= number1/number2
    else:
        result= number1-number2
    return result

print(__name__)

if __name__ == "__main__":
    app.run(debug=True)