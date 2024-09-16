def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_char = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_char + shift) % 26 + shift_char)
        else:
            encrypted_text += char  # Non-alphabetical characters remain the same
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just reverse shifting

# User input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

# Encryption
encrypted_message = encrypt(message, shift_value)
print(f"Encrypted Message: {encrypted_message}")

# Decryption
decrypted_message = decrypt(encrypted_message, shift_value)
print(f"Decrypted Message: {decrypted_message}")
