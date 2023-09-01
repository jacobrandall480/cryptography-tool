from affine import AffineCipher
from caesar import CaesarCipher
from vigenere import VigenereCipher

import argparse
import os
import sys
import math
import string

characters = string.ascii_letters + string.digits + string.punctuation
m = len(characters) + 1

def main():
    args = parse_args(sys.argv[1:])
    validate_args(args)
    get_cipher(args)
    key = get_key(args)
    # activates cipher
    if args.cipher == "affine":
        if math.gcd(key[0], m) != 1:
            sys.exit(f"Invalid Key: a and m ({m}) must be coprimes")
        else:
            cipher = AffineCipher(key)
    elif args.cipher == "caesar":
        cipher = CaesarCipher(key)
    elif args.cipher == "vigenere":
        cipher = VigenereCipher(key)

    get_mode(args)

    # get message to encrypt/decrypt
    input_text = handle_input(args)

    # determines what output looks like
    if args.mode == "encrypt":
        ciphertext = cipher.encrypt(input_text)
        if args.outfile:
            handle_output(args, ciphertext)
        else:
            print(f"Ciphertext: {handle_output(args, ciphertext)}\n")
    else:
        plaintext = cipher.decrypt(input_text)
        if args.outfile:
            handle_output(args, plaintext)
        else:
            print(f"Plaintext: {handle_output(args, plaintext)}\n")


# posible command-line interface args
def parse_args(args):
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt message")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], help="Action")
    parser.add_argument("-c", "--cipher", choices=["affine", "caesar", "vigenere"], help="Cipher algorithm")
    parser.add_argument("-k", "--key", type=str, help="Encryption/Decryption key")
    parser.add_argument("-i", "--infile", type=str, help="Input file")
    parser.add_argument("-o", "--outfile", type=argparse.FileType("w"), help="Output file")
    return parser.parse_args(args)

def validate_args(args):
    # checks files
    if args.infile:
        if not os.path.exists(args.infile):
            sys.exit(f"{args.infile} does not exist!")

        ext = os.path.splitext(args.infile)[1]
        if ext != ".txt":
            sys.exit(f"File must have .txt extension")
        infile = open(args.infile, "r")

    if args.outfile:
        ext = os.path.splitext(args.outfile.name)[1]
        if ext != ".txt":
            os.remove(args.outfile.name) # removes invalid file
            sys.exit(f"File must have .txt extension")

    # checks keys
    if args.key:
        # ensures that affine cipher key is two ints
        if args.cipher == "affine":
            try:
                a, b = map(int, args.key.split(","))
            except:
                sys.exit("Affine Cipher Key Usage: -k int_a,int_b")
        # ensures that caesar cipher key is an int
        elif args.cipher == "caesar":
            if not args.key.isdigit():
                sys.exit("Caesar Cipher Key Usage: -k postive_int")
            if args.key.isdigit() and int(args.key) < 1:
                sys.exit("Caesar Cipher Key Usage: -k postive_int")

        if not args.cipher:
            sys.exit("Cannot validate key without cipher")

# if given infile read text from it, otherwise input text
def handle_input(args):
    if args.infile:
        with open(args.infile, "r") as infile:
            text = infile.read()
            text = text.replace("\n", " ")
    else:
        if args.mode == "encrypt":
            text = input("\nEnter plaintext: ")
        else:
            text = input("\nEnter ciphertext: ")
    return text

# if given outfile writes output there, otherwise goes to terminal
def handle_output(args, text):
    if args.outfile:
        with open(args.outfile.name, "w") as outfile:
            outfile.write(text)
    else:
        return text

def get_mode(args):
    # interactive if no mode specified
    if not args.mode:
        while True:
            mode = input("\n1. Encrypt\n2. Decrypt\nEnter mode: ")
            if mode == "1":
                args.mode = "encrypt"
                break
            elif mode == "2":
                args.mode = "decrypt"
                break
            else:
                print("Invalid input. Please try again.\n")

def get_cipher(args):
    # interactive if no cipher specified
    if not args.cipher:
        while True:
            cipher = input("\n1. Affine Cipher\n2. Caesar Cipher\n3. Vigenere Cipher\nEnter cipher: ")
            if cipher == "1":
                args.cipher = "affine"
                break
            elif cipher == "2":
                args.cipher = "caesar"
                break
            elif cipher == "3":
                args.cipher = "vigenere"
                break
            else:
                print("Invalid input. Please try again.\n")



def get_key(args):
    while True:
        if not args.key:
            # ensures that a and b are ints for affine cipher
            if args.cipher == "affine":
                try:
                    a = input("\nEnter a: ")
                    b = input("Enter b: ")
                    key = [int(a), int(b)]
                except:
                    print("a and b must be integers")
                    continue
            # ensures key for caesar cipher is an int
            elif args.cipher == "caesar":
                try:
                    key = int(input("\nEnter key: "))
                    if key < 1:
                        print("Key must be a positive integer")
                        continue
                except:
                    print("Key must be a positive integer")
                    continue
            # no restrictions for vigenere cipher
            else:
                key = input("\nEnter key: ")
        else:
            if args.cipher == "affine":
                a, b = map(int, args.key.split(","))
                key = [a, b]
            else:
                key = args.key
        return key

if __name__ == "__main__":
    main()
