# modified Vigenere cipher - encrypts all characters; case sensitive


class VigenereCipher:

    def __init__(self, key):
        self.key = key

    # vigenere encryption for all characters
    def encrypt(self, plaintext):
        key_num = [ord(i) for i in self.key]
        plaintext_num = [ord(i) for i in plaintext]
        ciphertext = ""

        for i in range(len(plaintext_num)):
            c = key_num[i % len(self.key)]
            encrypted_c = (plaintext_num[i] - 32 + c) % 95
            ciphertext += chr(encrypted_c + 32)
        return ciphertext

    # vigenere decryption for all characters
    def decrypt(self, ciphertext):
        key_num = [ord(i) for i in self.key]
        ciphertext_num = [ord(i) for i in ciphertext]
        plaintext = ""

        for i in range(len(ciphertext_num)):
            c = key_num[i % len(self.key)]
            decrypted_c = (ciphertext_num[i] - 32 - c) % 95
            plaintext += chr(decrypted_c + 32)
        return plaintext


def main():
    message = input("Message: ")
    key = input("Key: ")

    cipher = VigenereCipher(key)

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