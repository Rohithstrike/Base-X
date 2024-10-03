from flask import Flask, request, jsonify, render_template
from main import *  # Ensure to import your main functions

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

    # Check for valid action
    if action not in ['encode', 'decode']:
        return jsonify({'error': 'Invalid action selected'}), 400

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
        'base30': base30,
        'base31': base31,
        'base32': base32,
        'base33': base33,
        'base34': base34,
        'base35': base35,
        'base36': base36,
        'base37': base37,
        'base38': base38,
        'base39': base39,
        'base40': base40,
        'base41': base41,
        'base42': base42,
        'base43': base43,
        'base44': base44,
        'base45': base45,
        'base46': base46,
        'base47': base47,
        'base48': base48,
        'base49': base49,
        'base50': base50,
        'base51': base51,
        'base52': base52,
        'base53': base53,
        'base54': base54,
        'base55': base55,
        'base56': base56,
        'base57': base57,
        'base58': base58,
        'base59': base59,
        'base60': base60,
        'base61': base61,
        'base62': base62,
        'base63': base63,
        'base64': base64_custom,  # Ensure this is defined in your main module
        'base65': base65,
        'base66': base66,
        'base67': base67,
        'base68': base68,
        'base69': base69,
        'base70': base70,
        'base71': base71,
        'base72': base72,
        'base73': base73,
        'base74': base74,
        'base75': base75,
        'base76': base76,
        'base77': base77,
        'base78': base78,
        'base79': base79,
        'base80': base80,
        'base81': base81,
        'base82': base82,
        'base83': base83,
        'base84': base84,
        'base85': base85,
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