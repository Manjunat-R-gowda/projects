
import random
from art import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def cesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabets:
            cipher_text += letter
        else:
            shift_pos = alphabets.index(letter) + shift_amount
            shift_pos %= len(alphabets)
            cipher_text += alphabets[shift_pos]

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


should_continue = True

while should_continue:

    direction = input(
        "Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type your shift number:\n"))

    cesar(text, shift, direction)

    continue_game = input(
        "Should you continue the game? Type 'yes' or 'no':\n").lower()

    if continue_game == "no":
        should_continue = False
        print("Goodbye!")

           
