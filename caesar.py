# modified Caesar cipher - encrypts all characters; case sensitive
# alphanumeric cycle through each other (lowercase -> uppercase -> digits), ie 'z' -> 'A', 'Z' -> '0', '9' -> 'a'
# special characters cycle through each other based on ASCII code
import string

class CaesarCipher:
    def __init__(self, key):
        self.key = key

        self.alnums = string.ascii_letters + string.digits #alphanumerics
        self.specials = string.punctuation + " " #special characters, including spaces

    def encrypt(self, plaintext):
        ciphertext = ""
        for c in plaintext:
            # checks if alphanumeric
            if c.isalnum():
                idx = self.alnums.index(c)
                idx += int(self.key)
                idx %= len(self.alnums)
                ciphertext += self.alnums[idx]
            # checks if special character
            elif c in self.specials:
                idx = self.specials.index(c)
                idx += int(self.key)
                idx %= len(self.specials)
                ciphertext += self.specials[idx]
        return ciphertext


    def decrypt(self, ciphertext):
        plaintext = ""

        for i,c in enumerate(ciphertext):
            # checks if alphanumeric
            if c.isalnum():
                idx = self.alnums.index(c)
                idx -= int(self.key)
                idx %= len(self.alnums)
                plaintext += self.alnums[idx]
            # checks if special character
            elif c in self.specials:
                idx = self.specials.index(c)
                idx -= int(self.key)
                idx %= len(self.specials)
                plaintext += self.specials[idx]
        return plaintext

def main():

    message = input("Message: ")
    while True:
        key = input("Key: ")
        if int(key) > 0:
            break
        print("Key must be a positive integer.")
    cipher = CaesarCipher(key)

    choice = int(input('Option:\n1. Encryption\n2. Decryption\n'))
    if choice == 1:
        # calling encryption function
        ciphertext = cipher.encrypt(message)

        print('Your encrypted text is the following: {}'.format(ciphertext))
    else:
        # calling decryption function
        print('Your decrypted text is the following: {}'.format
               (cipher.decrypt(message)))

if __name__ == "__main__":
    main()