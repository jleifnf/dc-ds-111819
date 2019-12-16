import string

SHIFT = 3
CHOICE = input("would you like to encode or decode?")
WORD = input("Please enter text")
LETTERS = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if CHOICE == "encode":
    for letter in WORD:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) +
                 SHIFT)
            encoded = encoded + LETTERS[x]
if CHOICE == "decode":
    for letter in WORD:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = LETTERS.index(letter) - SHIFT
            encoded = encoded + LETTERS[x]

print(encoded)
