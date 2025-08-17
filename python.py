MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B',
    '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W',
    '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?',
    '-.-.--': '!', '-....-': '-', '-..-.': '/',
    '.--.-.': '@', '-.--.': '(', '-.--.-': ')'
}

def decode_morse(morse_code):
    words = morse_code.strip().split("   ")
    decoded_words = []
    for word in words:
        letters = word.split(" ")
        decoded_word = "".join(MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)

if __name__ == "__main__":
    with open("morse.txt", "r") as f:
        morse_text = f.read().strip()
    if " " not in morse_text:
        morse_symbols = [morse_text[i:i+3] for i in range(0, len(morse_text), 3)]
        morse_text = " ".join(morse_symbols)

    print("Obtained Morse symbols:", morse_text)
    decoded_text = decode_morse(morse_text)
    print("Decoded Text:", decoded_text if decoded_text else "[No valid Morse symbols decoded]")
