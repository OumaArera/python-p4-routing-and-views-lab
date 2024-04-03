# Import necessary modules
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Define routes and views

# Index view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string view
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

# Count view
@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(num + 1))  # Include the upper limit
    return numbers

# Math view
@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'
    
    return str(result)

# Run the application
if __name__ == '__main__':
    app.run(port=5555)
