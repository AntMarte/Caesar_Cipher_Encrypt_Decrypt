def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            ascii_offset = ord('a') if char.islower() else ord('A')  # Determine the ASCII offset based on the letter case
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)  # Apply the shift to the character
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Non-letter characters remain unchanged
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decryption is simply encryption with a negated shift value

def main():
    choice = input("Choose an operation (encrypt/decrypt): ").lower()
    if choice == "encrypt":
        plaintext = input("Enter the plaintext: ")
        shift = int(input("Enter the shift value: "))
        ciphertext = caesar_encrypt(plaintext, shift)
        print("Ciphertext:", ciphertext)
    elif choice == "decrypt":
        ciphertext = input("Enter the ciphertext: ")
        shift = int(input("Enter the shift value: "))
        plaintext = caesar_decrypt(ciphertext, shift)
        print("Plaintext:", plaintext)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
