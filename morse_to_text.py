# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '/': ' '
}

def morse_to_text(morse_code):
    morse_code = morse_code.split()
    text = []
    for code in morse_code:
        if code in MORSE_CODE_DICT:
            text.append(MORSE_CODE_DICT[code])
        else:
            text.append('?')  # Placeholder for unknown characters
    return ''.join(text)

if __name__ == "__main__":
    morse_code = input("Enter Morse code to convert to text: ")
    text = morse_to_text(morse_code)
    print(f"Text: {text}")

