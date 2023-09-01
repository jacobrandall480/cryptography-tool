# modified Affine cipher - encrypts all characters; case sensitive

import string
import math
import sys

characters = string.ascii_letters + string.digits + string.punctuation # valid characters
m = len(characters) + 1 # size of valid characters

class AffineCipher:
    def __init__(self, key):

        self.key = key #[a, b]
        
        # ensures a and m are coprime
        if math.gcd(self.key[0], m) != 1:
            sys.exit(f"Invalid Key: a and m ({m}) must be coprimes")


    def encrypt(self, plaintext):
        # C = (a * P + b) % length_of_character_set

        return ''.join([chr(((self.key[0] * (ord(c) - ord(" ")) + self.key[1]) % m)
                            + ord(" ")) for c in plaintext])


    def decrypt(self, ciphertext):
        # P = (a^-1 * (C - b)) % length_of_character_set

        return ''.join([chr(((mod_inv(self.key[0], m) * (ord(c) - ord(" ") - self.key[1])) % m)
                            + ord(" ")) for c in ciphertext])


# Euclidian Algorithm for finding gcd
def euclid_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

# Modular multiplicative inverse
def mod_inv(a, MOD):
    gcd, x, y = euclid_gcd(a, MOD)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % MOD


def main():
    a = int(input("Enter Key A: "))
    b = int(input("Enter Key B: "))
    key = [a, b]

    cipher = AffineCipher(key)

    message = input("Enter message: ")

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
