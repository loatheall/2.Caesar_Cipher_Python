alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
text = input("Type your message:\n ").lower()
shift = int(input("Type the shift number:\n "))



# TODO-1: Create a function 'encrypt()' that takes "original_text" and 'shift_amount' as 2 inputs
def encrypt(original_text, shift_amount):

    cipher_text = ""

# TODO-2: Inside encrypt() function, shift each letter of the 'original_text' and shift each letter in a alphabet-
# TODO-2: by the shift amount and print the encrypted text use index()
    for i in range(len(original_text)):

        number = alphabet.index(original_text[i])
        index_after_shift = number + shift_amount

        # TODO-4: What happens if you try to shift z, can you fix the code?
        index_after_shift %= len(alphabet)

        cipher_text += alphabet[index_after_shift]
        print(f"Here is the encoded result: {cipher_text}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs
encrypt(original_text=text, shift_amount=shift)
