from project import *
# parse_args, validate_args, handle_input, handle_output, get_mode,
# get_cipher, get_key, AffineCipher, CaesarCipher, VigenereCipher
import pytest
from unittest import mock

def test_parse_args():
    # valid arguments
    args = parse_args(["-m", "encrypt", "-c", "vigenere", "-k", "h2!", "-i", "test.txt", "-o", "testout.txt"])
    assert args.mode == "encrypt"
    assert args.cipher == "vigenere"
    assert args.key == "h2!"
    assert args.infile == "test.txt"
    assert args.outfile.name == "testout.txt"

def test_validate_args():
    args = parse_args(["-m", "encrypt", "-c", "vigenere", "-k", "h2!"])
    validate_args(args) # should not raise exceptions or exit

    # test invalid args
    with pytest.raises(SystemExit):
        # input file does not exist
        args = parse_args(["-i", "nonexistent.txt"])
        validate_args(args)

    with pytest.raises(SystemExit):
        # input file, wrong extension
        args = parse_args(["-i", "test.csv"])
        validate_args(args)

    with pytest.raises(SystemExit):
        # output file, wrong extension
        args = parse_args(["-o", "output.jpg"])
        validate_args(args)

    with pytest.raises(SystemExit):
        # affine cipher key is not two ints
        args = parse_args(["-c", "affine", "-k", "a,b"])
        validate_args(args)

    with pytest.raises(SystemExit):
        # caesar cipher key is not a pos int
        args = parse_args(["-c", "caesar", "-k", "-12"])
        validate_args(args)

        args = parse_args(["-c", "caesar", "-k", "a"])
        validate_args(args)

    with pytest.raises(SystemExit):
        # key without cipher
        args = parse_args(["-k", "3"])
        validate_args(args)


def test_handle_input(monkeypatch):
    # input from file
    args = parse_args(["-m", "encrypt", "-c", "caesar", "-k", "3", "-i", "plaintext.txt"])
    with open("plaintext.txt") as file:
        text = file.read()
        text = text.replace("\n", " ")
    assert handle_input(args) == text # should read text from plaintext.txt

    # input from terminal
    args = parse_args(["-m", "encrypt", "-c", "caesar", "-k", "3"])
    text = "Hello World"
    monkeypatch.setattr("builtins.input", lambda x: text)
    assert handle_input(args) == text # should read text from input()

def test_handle_output():
    # output to file
    args = parse_args(["-m", "encrypt", "-c", "caesar", "-k", "3", "-o", "out.txt"])
    text = "Hello World"
    handle_output(args, text) # should write text to file
    with open("out.txt") as file:
        assert file.read() == text

    # output to terminal
    args = parse_args(["-m", "encrypt", "-c", "caesar", "-k", "3"])
    text = "123 !@#"
    assert handle_output(args, text) == text # should return text as string

def test_get_mode():
    # valid args
    args = parse_args(["-m", "encrypt"])
    get_mode(args) # should not ask for input
    assert args.mode == "encrypt"

    args = parse_args(["-m", "decrypt"])
    get_mode(args) # should not ask for input
    assert args.mode == "decrypt"

    # interactive mode
    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["1"]):
        get_mode(args) # should ask for input and accept 1
        assert args.mode == "encrypt"

    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["2"]):
        get_mode(args) # should ask for input and accept 2
        assert args.mode == "decrypt"

    # invalid inputs
    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["3", "1"]):
        get_mode(args) # should ask for input and reject 3, then accept 1
        assert args.mode == "encrypt"

    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["a", "2"]):
        get_mode(args) # should ask for input and reject a, then accept 2
        assert args.mode == "decrypt"


def test_get_cipher():
    # valid args
    args = parse_args(["-c", "affine"])
    get_cipher(args) # should not ask for input
    assert args.cipher == "affine"

    args = parse_args(["-c", "caesar"])
    get_cipher(args) # should not ask for input
    assert args.cipher == "caesar"

    args = parse_args(["-c", "vigenere"])
    get_cipher(args) # should not ask for input
    assert args.cipher == "vigenere"

    # interactive mode
    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["1"]):
        get_cipher(args) # should ask for input and accept 1
        assert args.cipher == "affine"

    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["2"]):
        get_cipher(args) # should ask for input and accept 2
        assert args.cipher == "caesar"

    # invalid inputs
    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["3"]):
        get_cipher(args) # should ask for input and reject 3, then accept 1
        assert args.cipher == "vigenere"

    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["4", "1"]):
        get_cipher(args) # should ask for input and reject a, then accept 1
        assert args.cipher == "affine"

    args = parse_args([])
    with mock.patch("builtins.input", side_effect=["a", "2"]):
        get_cipher(args) # should ask for input and reject a, then accept 2
        assert args.cipher == "caesar"

def test_get_key():
    # valid args
    args = parse_args(["-c", "affine", "-k", "37,12"])
    key = get_key(args) # should not ask for input
    assert key == [37, 12]

    args = parse_args(["-c", "caesar", "-k", "12"])
    key = get_key(args) # should not ask for input
    assert key == "12"

    args = parse_args(["-c", "vigenere", "-k", "h2!"])
    key = get_key(args) # should not ask for input
    assert key == "h2!"

    # interactive mode
    args = parse_args(["-c", "affine"])
    with mock.patch("builtins.input", side_effect=["37", "12"]):
        key = get_key(args) # should ask for input and accept 37, 12
        assert key == [37, 12]

    args = parse_args(["-c", "caesar"])
    with mock.patch("builtins.input", side_effect=["12"]):
        key = get_key(args) # should ask for input and accept 12
        assert key == 12

    args = parse_args(["-c", "vigenere"])
    with mock.patch("builtins.input", side_effect=["h2!"]):
        key = get_key(args) # should ask for input and accept h2!
        assert key == "h2!"

    # invalid inputs
    args = parse_args(["-c", "affine"])
    with mock.patch("builtins.input", side_effect=["a", "b", "37", "12"]):
        key = get_key(args) # should ask for input and reject a, b then accept 37, 12
        assert key == [37, 12]

    args = parse_args(["-c", "caesar"])
    with mock.patch("builtins.input", side_effect=["-12", "0", "a", "12"]):
        key = get_key(args) # should ask for input and reject -12, 0, and a, then accept 12
        assert key == 12



def test_affine():
    cipher = AffineCipher([37,12])

    # lowercase
    assert cipher.encrypt("abc") == "Jo5"
    assert cipher.decrypt("Jo5") == "abc"

    # uppercase
    assert cipher.encrypt("ABC") == "}Ch"
    assert cipher.decrypt("}Ch") == "ABC"

    # digits
    assert cipher.encrypt("123") == "g-R"
    assert cipher.decrypt("g-R") == "123"

    assert cipher.encrypt("90") == "rB"
    assert cipher.decrypt("rB") == "90"

    # punctuation
    assert cipher.encrypt("!@#") == "QX<"
    assert cipher.decrypt("QX<") == "!@#"

    assert cipher.encrypt("|}~") == "{Af"
    assert cipher.decrypt("{Af") == "|}~"


def test_caesar():
    cipher = CaesarCipher(4)

    # lowercase
    assert cipher.encrypt("abc") == "efg"
    assert cipher.decrypt("efg") == "abc"

    # uppercase
    assert cipher.encrypt("ABC") == "EFG"
    assert cipher.decrypt("EFG") == "ABC"

    # digits
    assert cipher.encrypt("234") == "678"
    assert cipher.decrypt("678") == "234"

    # punctuation
    assert cipher.encrypt("!@#") == "%^'"
    assert cipher.decrypt("%^'") == "!@#"

    # wrap
    assert cipher.encrypt("xyz") == "BCD"
    assert cipher.decrypt("BCD") == "xyz"

    assert cipher.encrypt("XYZ") == "123"
    assert cipher.decrypt("123") == "XYZ"

    assert cipher.encrypt("90") == "d4"
    assert cipher.decrypt("d4") == "90"

    assert cipher.encrypt("zZ9") == "D3d"
    assert cipher.decrypt("D3d") == "zZ9"

    assert cipher.encrypt("|}~") == "!\"#"
    assert cipher.decrypt("!\"#") == "|}~"


def test_vigenere():
    cipher = VigenereCipher("h2!")

    # lowercase
    assert cipher.encrypt("abc") == "j5%"
    assert cipher.decrypt("j5%") == "abc"

    # uppercase
    assert cipher.encrypt("ABC") == "Jtd"
    assert cipher.decrypt("Jtd") == "ABC"

    # digits
    assert cipher.encrypt("123") == ":dT"
    assert cipher.decrypt(":dT") == "123"

    assert cipher.encrypt("90") == "Bb"
    assert cipher.decrypt("Bb") == "90"

    # punctuation
    assert cipher.encrypt("!@#") == "*rD"
    assert cipher.decrypt("*rD") == "!@#"

    assert cipher.encrypt("|}~") == "&P@"
    assert cipher.decrypt("&P@") == "|}~"