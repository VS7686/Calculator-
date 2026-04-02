from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'result': 'Error: Cannot divide by zero'})
        result = num1 / num2

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)