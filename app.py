from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_decimal', methods=['GET'])
def generate_decimal():
    decimal = random.randint(0, 255)  # Generate a random decimal between 0 and 255
    return jsonify({
        'decimal': decimal,
        'binary': format(decimal, '08b')  # Convert to 8-bit binary string
    })

if __name__ == '__main__':
    app.run(debug=True)
    