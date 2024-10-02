import string
import base64 as b64  # Import the built-in base64 library with an alias to avoid naming conflicts

# Characters allowed for encoding in bases 2 to 65 (digits, letters, and additional symbols)
BASE_CHARS = (
    string.digits +               # 0-9 (10)
    string.ascii_uppercase +      # A-Z (26)
    string.ascii_lowercase +      # a-z (26)
    "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"  # 32 additional symbols (total of 62)
)

# Ensure that BASE_CHARS has enough characters for up to base 65
if len(BASE_CHARS) < 65:
    raise ValueError("BASE_CHARS must have at least 65 unique characters.")

# Convert an integer to a given base
def to_base(num, base):
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(BASE_CHARS[num % base])
        num //= base
    return ''.join(digits[::-1])

# Convert a string representation of a number in a given base to an integer
def from_base(s, base):
    return sum(BASE_CHARS.index(char) * (base ** i) for i, char in enumerate(reversed(s)))

# Helper function to calculate byte length needed for decoding
def get_byte_length(number):
    return (number.bit_length() + 7) // 8

# Base N Encoding and Decoding (Generalized for base 2 to 65)
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

# Base64 Encoding and Decoding using standard library
def base64_encode(input_string):
    return b64.b64encode(input_string.encode()).decode()

def base64_decode(input_string):
    return b64.b64decode(input_string).decode(errors='ignore')

# Base encoding and decoding functions for bases 2 to 65
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

def base31(input_string, action):
    return baseN(input_string, action, 31)

def base32(input_string, action):
    return baseN(input_string, action, 32)

def base33(input_string, action):
    return baseN(input_string, action, 33)

def base34(input_string, action):
    return baseN(input_string, action, 34)

def base35(input_string, action):
    return baseN(input_string, action, 35)

def base36(input_string, action):
    return baseN(input_string, action, 36)

def base37(input_string, action):
    return baseN(input_string, action, 37)

def base38(input_string, action):
    return baseN(input_string, action, 38)

def base39(input_string, action):
    return baseN(input_string, action, 39)

def base40(input_string, action):
    return baseN(input_string, action, 40)

def base41(input_string, action):
    return baseN(input_string, action, 41)

def base42(input_string, action):
    return baseN(input_string, action, 42)

def base43(input_string, action):
    return baseN(input_string, action, 43)

def base44(input_string, action):
    return baseN(input_string, action, 44)

def base45(input_string, action):
    return baseN(input_string, action, 45)

def base46(input_string, action):
    return baseN(input_string, action, 46)

def base47(input_string, action):
    return baseN(input_string, action, 47)

def base48(input_string, action):
    return baseN(input_string, action, 48)

def base49(input_string, action):
    return baseN(input_string, action, 49)

def base50(input_string, action):
    return baseN(input_string, action, 50)

def base51(input_string, action):
    return baseN(input_string, action, 51)

def base52(input_string, action):
    return baseN(input_string, action, 52)

def base53(input_string, action):
    return baseN(input_string, action, 53)

def base54(input_string, action):
    return baseN(input_string, action, 54)

def base55(input_string, action):
    return baseN(input_string, action, 55)

def base56(input_string, action):
    return baseN(input_string, action, 56)

def base57(input_string, action):
    return baseN(input_string, action, 57)

def base58(input_string, action):
    return baseN(input_string, action, 58)

def base59(input_string, action):
    return baseN(input_string, action, 59)

def base60(input_string, action):
    return baseN(input_string, action, 60)

def base61(input_string, action):
    return baseN(input_string, action, 61)

def base62(input_string, action):
    return baseN(input_string, action, 62)

def base63(input_string, action):
    return baseN(input_string, action, 63)

def base64_custom(input_string, action):
    if action == 'encode':
        return base64_encode(input_string)
    elif action == 'decode':
        return base64_decode(input_string)

def base65(input_string, action):
    return baseN(input_string, action, 65)