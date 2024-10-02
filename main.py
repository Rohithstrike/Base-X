import string

# Characters allowed for encoding in bases 2 to 36 (digits and letters)
BASE_CHARS = string.digits + string.ascii_uppercase

# Convert an integer to a given base
def to_base(num, base):
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(BASE_CHARS[num % base])  # Use the correct character set
        num //= base
    return ''.join(digits[::-1])

# Convert a string representation of a number in a given base to an integer
def from_base(s, base):
    return sum(BASE_CHARS.index(char) * (base ** i) for i, char in enumerate(reversed(s)))

# Helper function to calculate byte length needed for decoding
def get_byte_length(number):
    return (number.bit_length() + 7) // 8

# Base N Encoding and Decoding (Generalized for base 2 to base 30)
def baseN(input_string, action, base):
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

# Base encoding and decoding functions for bases 2 to 30
def base2(input_string, action):
    return baseN(input_string, action, 2)

def base3(input_string, action):
    return baseN(input_string, action, 3)

def base4(input_string, action):
    return baseN(input_string, action, 4)

def base5(input_string, action):
    return baseN(input_string, action, 5)

def base6(input_string, action):
    return baseN(input_string, action, 6)

def base7(input_string, action):
    return baseN(input_string, action, 7)

def base8(input_string, action):
    return baseN(input_string, action, 8)

def base9(input_string, action):
    return baseN(input_string, action, 9)

def base10(input_string, action):
    return baseN(input_string, action, 10)

def base11(input_string, action):
    return baseN(input_string, action, 11)

def base12(input_string, action):
    return baseN(input_string, action, 12)

def base13(input_string, action):
    return baseN(input_string, action, 13)

def base14(input_string, action):
    return baseN(input_string, action, 14)

def base15(input_string, action):
    return baseN(input_string, action, 15)

def base16(input_string, action):
    if action == 'encode':
        return input_string.encode().hex()  # Hex encoding
    elif action == 'decode':
        return bytes.fromhex(input_string).decode(errors='ignore')

def base17(input_string, action):
    return baseN(input_string, action, 17)

def base18(input_string, action):
    return baseN(input_string, action, 18)

def base19(input_string, action):
    return baseN(input_string, action, 19)

def base20(input_string, action):
    return baseN(input_string, action, 20)

def base21(input_string, action):
    return baseN(input_string, action, 21)

def base22(input_string, action):
    return baseN(input_string, action, 22)

def base23(input_string, action):
    return baseN(input_string, action, 23)

def base24(input_string, action):
    return baseN(input_string, action, 24)

def base25(input_string, action):
    return baseN(input_string, action, 25)

def base26(input_string, action):
    return baseN(input_string, action, 26)

def base27(input_string, action):
    return baseN(input_string, action, 27)

def base28(input_string, action):
    return baseN(input_string, action, 28)

def base29(input_string, action):
    return baseN(input_string, action, 29)

def base30(input_string, action):
    return baseN(input_string, action, 30)