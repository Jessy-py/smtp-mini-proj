alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#creating the function that takes the 'text' and 'shift' inputs
# def encrypt(plain_text, shift_amount):
#     cypher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
#     print(f"The encoded text is {cypher_text}.")

# def decrypt(de_text, de_shift):
#     actual_text = ""
#     for letter in de_text:
#         position = alphabet.index(letter)
#         actual_position = position - de_shift
#         actual_letter = alphabet[actual_position]
#         actual_text += actual_letter
#     print(f"The decoded text is {actual_text}.")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(de_text=text, de_shift=shift)

def ceaser(my_text, my_shift, my_direction):
    actual_text = ""
    if my_direction == "decode":
        my_shift *= -1
    for letter in my_text:
        position = alphabet.index(letter)
        new_position = position + my_shift
        actual_text += alphabet[new_position]
    print(f"The {my_direction}d text is {actual_text}.")

ceaser(my_text=text, my_shift=shift, my_direction=direction)


