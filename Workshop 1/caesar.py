class Caesar:
    def __init__(self, steps):
        self._steps = steps

    def encrypt(self, plaintext):
        cipher = " "
        for letter in str(plaintext):
            letter.lower()
            if letter == " ":
                cipher += " "
            else:
                new_letter = chr(ord(letter) + self._steps)
                cipher += new_letter
        return cipher

    def decrypt(self, cipher):
        plaintext = " "
        for letter in str(cipher):
            letter.lower()
            if letter == " ":
                plaintext += " "
            else:
                new_letter = chr(ord(letter) - self._steps)
                plaintext += new_letter
        return plaintext
