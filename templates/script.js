async function processAction(action) {
    const base = document.getElementById('baseSelect').value;
    const inputString = document.getElementById('inputString').value;
    let outputString = '';

    try {
        switch (base) {
            case 'base2':
                outputString = action === 'encode' ? encodeBase2(inputString) : decodeBase2(inputString);
                break;
            case 'base3':
                outputString = action === 'encode' ? encodeBase3(inputString) : decodeBase3(inputString);
                break;
            case 'base8':
                outputString = action === 'encode' ? encodeBase8(inputString) : decodeBase8(inputString);
                break;
            case 'base10':
                outputString = action === 'encode' ? encodeBase10(inputString) : decodeBase10(inputString);
                break;
            case 'base16':
                outputString = action === 'encode' ? encodeBase16(inputString) : decodeBase16(inputString);
                break;
            case 'base32':
                outputString = action === 'encode' ? encodeBase32(inputString) : decodeBase32(inputString);
                break;
            case 'base36':
                outputString = action === 'encode' ? encodeBase36(inputString) : decodeBase36(inputString);
                break;
            case 'base58':
                outputString = action === 'encode' ? encodeBase58(inputString) : decodeBase58(inputString);
                break;
            case 'base64':
                outputString = action === 'encode' ? encodeBase64(inputString) : decodeBase64(inputString);
                break;
            case 'base85':
                outputString = action === 'encode' ? encodeBase85(inputString) : decodeBase85(inputString);
                break;
            case 'base91':
                outputString = action === 'encode' ? encodeBase91(inputString) : decodeBase91(inputString);
                break;
            case 'base122':
                outputString = action === 'encode' ? encodeBase122(inputString) : decodeBase122(inputString);
                break;
            case 'base256':
                outputString = action === 'encode' ? encodeBase256(inputString) : decodeBase256(inputString);
                break;
            default:
                throw new Error('Invalid base selected');
        }
    } catch (error) {
        outputString = `Error: ${error.message}`;
    }

    document.getElementById('outputString').value = outputString;
}

function encodeBase2(str) {
    return [...str].map(char => char.charCodeAt(0).toString(2)).join(' ');
}

function decodeBase2(str) {
    return str.split(' ').map(bin => String.fromCharCode(parseInt(bin, 2))).join('');
}

function encodeBase3(str) {
    return [...str].map(char => char.charCodeAt(0).toString(3)).join(' ');
}

function decodeBase3(str) {
    return str.split(' ').map(tri => String.fromCharCode(parseInt(tri, 3))).join('');
}

function encodeBase8(str) {
    return [...str].map(char => char.charCodeAt(0).toString(8)).join(' ');
}

function decodeBase8(str) {
    return str.split(' ').map(oct => String.fromCharCode(parseInt(oct, 8))).join('');
}

function encodeBase10(str) {
    return [...str].map(char => char.charCodeAt(0).toString(10)).join(' ');
}

function decodeBase10(str) {
    return str.split(' ').map(dec => String.fromCharCode(parseInt(dec, 10))).join('');
}

function encodeBase16(str) {
    return [...str].map(char => char.charCodeAt(0).toString(16)).join(' ');
}

function decodeBase16(str) {
    return str.split(' ').map(hex => String.fromCharCode(parseInt(hex, 16))).join('');
}

function encodeBase64(str) {
    return btoa(str);
}

function decodeBase64(str) {
    return atob(str);
}

// Placeholder functions for more complex encodings like Base32, Base58, Base85, etc.
// You may need to include external libraries or custom algorithms for these bases.

function encodeBase32(str) {
    return "Base32 encoding not implemented";
}

function decodeBase32(str) {
    return "Base32 decoding not implemented";
}

function encodeBase36(str) {
    return "Base36 encoding not implemented";
}

function decodeBase36(str) {
    return "Base36 decoding not implemented";
}

function encodeBase58(str) {
    return "Base58 encoding not implemented";
}

function decodeBase58(str) {
    return "Base58 decoding not implemented";
}

function encodeBase85(str) {
    return "Base85 encoding not implemented";
}

function decodeBase85(str) {
    return "Base85 decoding not implemented";
}

function encodeBase91(str) {
    return "Base91 encoding not implemented";
}

function decodeBase91(str) {
    return "Base91 decoding not implemented";
}

function encodeBase122(str) {
    return "Base122 encoding not implemented";
}

function decodeBase122(str) {
    return "Base122 decoding not implemented";
}

function encodeBase256(str) {
    return "Base256 encoding not implemented";
}

function decodeBase256(str) {
    return "Base256 decoding not implemented";
}
