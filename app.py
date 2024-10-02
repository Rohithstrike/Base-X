from flask import Flask, request, jsonify, render_template
from main import *  # Make sure to import your main functions

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the main HTML page
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Extract the JSON data from the request
    data = request.json
    base = data.get('base')
    input_string = data.get('inputString')
    action = data.get('action')

    # Dictionary to map bases to functions
    base_functions = {
        'base2': base2,
        'base3': base3,
        'base4': base4,
        'base5': base5,
        'base6': base6,
        'base7': base7,
        'base8': base8,
        'base9': base9,
        'base10': base10,
        'base11': base11,
        'base12': base12,
        'base13': base13,
        'base14': base14,
        'base15': base15,
        'base16': base16,
        'base17': base17,
        'base18': base18,
        'base19': base19,
        'base20': base20,
        'base21': base21,
        'base22': base22,
        'base23': base23,
        'base24': base24,
        'base25': base25,
        'base26': base26,
        'base27': base27,
        'base28': base28,
        'base29': base29,
        'base30': base30
    }

    # Check if the selected base is valid and call the corresponding function
    if base in base_functions:
        result = base_functions[base](input_string, action)
    else:
        return jsonify({'error': 'Invalid base selected'}), 400

    # Return the result in JSON format
    return jsonify({'result': result})

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)