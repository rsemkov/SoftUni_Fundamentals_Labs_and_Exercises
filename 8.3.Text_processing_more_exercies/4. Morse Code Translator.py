MORSE_CODE_DICT = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
}


def morse_decoder(encrypted_text):
    result = ""
    # SPLITS THE TEXT BY WORDS
    for word in text:
        word = word.split()
        # ADDS EACH LETTER TO THE RESULT AFTER DECODING IT. AFTER THE WHOLE WORD IS DONE, ADDS A WHITE SPACE
        for letter in word:
            result += MORSE_CODE_DICT[letter]
        # ADDS WHITE SPACE AFTER EACH WORD
        result += " "
    return result


text = input().split(" | ")
print(morse_decoder(text))
