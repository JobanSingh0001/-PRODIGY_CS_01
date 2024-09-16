# -PRODIGY_CS_01
How to Use:

    Input:
        You are prompted to enter a message.
        You then provide a shift value (an integer) for encryption.

    Output:
        The program encrypts the message using the shift value and prints the encrypted message.
        It also decrypts the encrypted message and prints the original message.

Example:

    Input:
        Message: Hello World
        Shift: 3
    Encrypted Output: Khoor Zruog
    Decrypted Output: Hello World

Code Summary:

    The code shifts letters according to their position in the alphabet (ASCII value).
    Non-alphabetic characters like spaces or punctuation remain unchanged.
    Decryption simply applies the reverse of the encryption process by shifting the letters backward.

