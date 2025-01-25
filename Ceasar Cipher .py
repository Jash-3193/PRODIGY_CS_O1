# Caesar Cipher Encryption and Decryption Program

# Function to encrypt the message
def encrypt(message, shift):
    encrypted_message = ""  # This will store the encrypted message
    for char in message:
        # Check if the character is an alphabet
        if char.isalpha():
            # Shift the character within the alphabet
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            # Non-alphabet characters remain the same
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, shift):
    decrypted_message = ""  # This will store the decrypted message
    for char in encrypted_message:
        # Check if the character is an alphabet
        if char.isalpha():
            # Shift the character back within the alphabet
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            # Non-alphabet characters remain the same
            decrypted_message += char
    return decrypted_message

# Main function to interact with the user
def main():
    print("Caesar Cipher Encryption and Decryption\n")
    
    # Get user input for the operation
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    
    # Get the message to encrypt or decrypt
    message = input("Enter the message: ")
    
    # Get the shift value must be an integer
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the shift value.")
        return
    
    # Perform encryption or decryption based on user choice
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice. Please choose either 'E' for encryption or 'D' for decryption.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
