from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'binary' in request.form:
            binary_input = request.form['binary']
            try:
                decimal = int(binary_input, 2)
                result = f" {binary_input} in binary is NOT {decimal} in decimal."
            except ValueError:
                result = "Invalid binary number. Please enter only 0s and 1s."
        elif 'decimal' in request.form:
            decimal_input = request.form['decimal']
            expected_binary = request.form['expected_binary']
            try:
                decimal = int(decimal_input)
                if bin(decimal)[2:] == expected_binary:
                    result = f"Correct!!! {decimal} in decimal is {expected_binary} in binary."
                    result = f"Incorrect. The binary representation of {decimal} is {bin(decimal)[2:]}."
                else:
                    result = f"Incorrect. The binary representation of {decimal} is {bin(decimal)[2:]}."
            except ValueError:
                result = "Invalid decimal number. Please enter a valid integer."
    return render_template('index.html', result=result)

@app.route('/generate_decimal', methods=['GET'])
def generate_decimal():
    decimal = random.randint(0, 255)  # Generate a random decimal between 0 and 255
    return jsonify({'decimal': decimal, 'binary': bin(decimal)[2:]})

if __name__ == '__main__':
    app.run(debug=True)
