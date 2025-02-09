import string
import base64 as b64
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Standard Base85/Ascii85 character set
BASE85_CHARS = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
)

# Extended character set for bases greater than 85, including all printable ASCII chars
EXTENDED_CHARS = (
    string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation + " "
)

# Base92 character set
BASE92_CHARS = (
    string.digits + string.ascii_uppercase + string.ascii_lowercase + "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)

# Ensure the base is within the valid range
def validate_base(base):
    if base < 2 or base > 100:
        raise ValueError("Base must be between 2 and 100.")

# Helper function to calculate byte length needed for decoding
def get_byte_length(number):
    return (number.bit_length() + 7) // 8

# Convert an integer to a string in the specified base
def to_base(num, base):
    validate_base(base)
    if num == 0:
        return '0'
    chars = BASE85_CHARS if base <= 85 else EXTENDED_CHARS
    digits = []
    while num:
        digits.append(chars[num % base])
        num //= base
    return ''.join(digits[::-1])

# Convert a string in a given base to an integer
def from_base(s, base):
    validate_base(base)
    chars = BASE85_CHARS if base <= 85 else EXTENDED_CHARS
    return sum(chars.index(char) * (base ** i) for i, char in enumerate(reversed(s)))

# Generalized Base N encoding and decoding
def baseN(input_string, action, base):
    validate_base(base)
    if action == 'encode':
        number = int.from_bytes(input_string.encode(), 'big')
        return to_base(number, base)
    elif action == 'decode':
        number = from_base(input_string, base)
        byte_length = get_byte_length(number)
        decoded_bytes = number.to_bytes(byte_length, 'big')
        try:
            return decoded_bytes.decode('utf-8').rstrip('\x00')
        except UnicodeDecodeError:
            return decoded_bytes.decode('latin-1', errors='ignore')

# Base64 Encoding and Decoding using the standard library
def base64_encode(input_string):
    return b64.b64encode(input_string.encode()).decode()

def base64_decode(input_string):
    return b64.b64decode(input_string).decode(errors='ignore')

# Ascii85 (Base85) Encoding and Decoding using standard library functions
def base85_encode(input_string):
    encoded_bytes = b64.a85encode(input_string.encode(), adobe=False)
    return encoded_bytes.decode()

def base85_decode(input_string):
    decoded_bytes = b64.a85decode(input_string, adobe=False)
    return decoded_bytes.decode()

# Flask API Route for Encoding/Decoding
@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        input_string = data.get("text", "")
        action = data.get("action", "encode")
        base = int(data.get("base", 10))
        
        if not input_string:
            return jsonify({"error": "No input text provided"}), 400
        
        if action == "encode":
            result = baseN(input_string, "encode", base)
        elif action == "decode":
            result = baseN(input_string, "decode", base)
        else:
            return jsonify({"error": "Invalid action"}), 400
        
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
