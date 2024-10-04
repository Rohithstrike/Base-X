import string
import base64 as b64

# Standard Base85/Ascii85 character set
BASE85_CHARS = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
)

# Extended character set for bases greater than 85, including all printable ASCII chars
EXTENDED_CHARS = (
    string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation + " "
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

# Base N encoding and decoding for different bases (2 to 100)
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
    return baseN(input_string, action, 16)

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

def base66(input_string, action):
    return baseN(input_string, action, 66)

def base67(input_string, action):
    return baseN(input_string, action, 67)

def base68(input_string, action):
    return baseN(input_string, action, 68)

def base69(input_string, action):
    return baseN(input_string, action, 69)

def base70(input_string, action):
    return baseN(input_string, action, 70)

def base71(input_string, action):
    return baseN(input_string, action, 71)

def base72(input_string, action):
    return baseN(input_string, action, 72)

def base73(input_string, action):
    return baseN(input_string, action, 73)

def base74(input_string, action):
    return baseN(input_string, action, 74)

def base75(input_string, action):
    return baseN(input_string, action, 75)

def base76(input_string, action):
    return baseN(input_string, action, 76)

def base77(input_string, action):
    return baseN(input_string, action, 77)

def base78(input_string, action):
    return baseN(input_string, action, 78)

def base79(input_string, action):
    return baseN(input_string, action, 79)

def base80(input_string, action):
    return baseN(input_string, action, 80)

def base81(input_string, action):
    return baseN(input_string, action, 81)

def base82(input_string, action):
    return baseN(input_string, action, 82)

def base83(input_string, action):
    return baseN(input_string, action, 83)

def base84(input_string, action):
    return baseN(input_string, action, 84)

def base85(input_string, action):
    if action == 'encode':
        return base85_encode(input_string)
    elif action == 'decode':
        return base85_decode(input_string)

def base86(input_string, action):
    return baseN(input_string, action, 86)

def base87(input_string, action):
    return baseN(input_string, action, 87)

def base88(input_string, action):
    return baseN(input_string, action, 88)

def base89(input_string, action):
    return baseN(input_string, action, 89)

def base90(input_string, action):
    return baseN(input_string, action, 90)

def base91(input_string, action):
    return baseN(input_string, action, 91)

def base92(input_string, action):
    return baseN(input_string, action, 92)

def base93(input_string, action):
    return baseN(input_string, action, 93)

def base94(input_string, action):
    return baseN(input_string, action, 94)

def base95(input_string, action):
    return baseN(input_string, action, 95)

def base96(input_string, action):
    return baseN(input_string, action, 96)

def base97(input_string, action):
    return baseN(input_string, action, 97)

def base98(input_string, action):
    return baseN(input_string, action, 98)

def base99(input_string, action):
    return baseN(input_string, action, 99)

def base100(input_string, action):
    return baseN(input_string, action, 100)
