alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
text = input("Type your message:\n ").lower()
shift = int(input("Type the shift number:\n "))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for i in range(len(original_text)):

        number = alphabet.index(original_text[i])
        index_after_shift = number + shift_amount

        index_after_shift %= len(alphabet)

        cipher_text += alphabet[index_after_shift]
        print(f"Here is the encoded result: {cipher_text}")

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs
def decrypt(original_text, shift_amount):
    cipher_text = ""

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' backwards in the alphabet
#  by the 'shift_amount' and print the decrypted text
    for i in range(len(original_text)):

        number = alphabet.index(original_text[i])
        index_after_shift = number - shift_amount

        index_after_shift %= len(alphabet)

        cipher_text += alphabet[index_after_shift]
    print(f"Here is the decoded result: {cipher_text}")
decrypt(original_text=text, shift_amount=shift)
