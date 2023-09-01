# MULTI-ALGORITHM CRYPTOGRAPHY TOOL
#### Video Demo:  <URL HERE>

## Definition
This project implements a command line tool for encrypting and decrypting text using classical cipher algorithms. Each cipher has been modified to allow for robust handling of case-sensitive letters, numbers, and special characters. Additionally, the project has the option of being completely interactive.

Project structure:
- affine.py - Implements affine cipher
- caesar.py - Implements caesar cipher
- vigenere.py - Implements vigenere cipher
- project.py - Main driver program
- test_project.py - Unit tests for cipher implementations and command line interface
- requirements.txt - Python dependencies
- README.md - Documentation

## Libraries
- **argparse** - For parsing command line arguments, link vv
- **math** - Provides mathematical functions
- **os** - Provides operating system functions
- **pytest** - Testing framework for validation
- **string** - For string constants and manipulation
- **sys** - Provides system functions and constants
- **unittest** - Unit testing framework

## Installation
Clone the repository:
```bash
git clone https://github.com/jacobrandall480/cryptography-project
```

There is a requirements.txt file that has all of the pip-installable libraries used, and can be simply installed by this pip command:
```bash
pip install -r requirements.txt
```

## Usage
**Command line options:**
- -m: mode (`encrypt` or `decrypt`)
- -c: cipher algorithm (`affine`, `caesar`, or `vigenere`)
- -k: encryption key (format depends on cipher)
- -i: input file
- -o: output file

Note: All command line arguments are optional, almost any combination of arguments can be used.

**Examples:**
#### Encrypt with affine cipher:
```bash
python project.py -m encrypt -c affine -k 37,12 -i plaintext.txt -o ciphertext.txt
```

#### Decrypt with vigenere cipher:
```bash
python project.py -m decrypt -c vigenere -k h2! -i ciphertext.txt -o plaintext.txt
```

#### Run interactive mode:
```bash
python project.py
```
The user is prompted to chose the mode:
```bash
1. Encrypt
2. Decrypt
Enter mode:
```
The user can choose either 1 or 2. Then they are prompted to choose a cipher algorithm:
``` bash
1. Affine Cipher
2. Caesar Cipher
3. Vigenere Cipher
Enter cipher:
```
The user can choose 1, 2, or 3. Then they are prompted to choose a key: <br>
- If using Caesar or Vigenere cipher:
    ```bash
    Enter key:
    ```
- If using Affine cipher:
    ```bash
    Enter a:
    Enter b:
    ```
Once the user inputs a valid key, they will be prompted to input their text and the result will print: <br>
- If mode is encrypt:
    ```bash
    Enter plaintext: [text]
    Ciphertext: [result]
    ```
- If mode is decrypt:
    ```bash
    Enter ciphertext: [text]
    Plaintext: [result]
    ```

**Guidance:**
- The input file `-i` should contain the text the user wants to encrypt or decrypt. If no infile is specified, the user will be prompted to input the text.
- The output file `-o` will contain the result. If no output file is specified, the result is printed to the console.
- Except for `-i` and `-o`, when running the program without a command line argument the user will be prompted to input the missing information. For an input or output file to be utilized it must be a command line argument.
    - ex) Encrypt with caesar cipher, get prompted for key and text, print result to console:
        ```bash
        python project.py -m encrypt -c caesar
        ```
- `-k` formatting: The affine cipher key must be two integers separated by a comma `37,12` not `37, 12` or `37 12`. The caesar cipher key must be a positive integer. The vigenere cipher key has no specific restrictions as any combination of letters, digits, and special characters can be used, but traditionally it is a string word such as `PASSWORD`.
    - Cannot use `-k` if `-c` is not used


### Description:
This project implements a command line encryption and decryption system using several classical cipher algorithms. Currently, the 3 supported ciphers are Affine, Caesar, Vigenère ciphers which have been optimized to include ASCII characters (dec.) 32 - 126.

Each cipher algorithm is implemented in a separate Python module with encrypt and decrypt functions The Affine cipher performs mathematical substituion based on modular arithmetic. It's key is two integers [a, b] of which a must be coprime to m (the length of the character set). The Caesar cipher shifts characters by a positive numeric value. The Vigenère cipher traditionally subsitutes characters with a keyword, but my version allows the key to include digits and special characters as well.

This program offers flexible options through the command line interface to select different cipher algorithms, encryption/decryption modes, keys, and input/output files. Robust input validation ensures the command line arguments are properly formatted before algorithm is performed.

The object-oriented design makes it easy to extend the tool with new cipher algorithms in the future. Unit tests validate the cipher implementations and command line argument handling.

To use the application, the user specifies the desired mode, cipher, key, input text, and output location via command line arguments or interactive user input. The input text is encrypted or decrypted (based on the mode) using the chosen cipher and key and then written to an output file or the console, depending on command line arguments.

Overall, this project demonstrates programming practices like modular design, command line interfaces, text processing, and unit testing.



## AUTHOR: Jacob Randall