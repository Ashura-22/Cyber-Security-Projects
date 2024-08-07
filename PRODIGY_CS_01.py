print('<-------------------Implement Caesar Cipher------------------->')
def caesar_cipher(text, shift):
    result = ""
    
    # Traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
    
    return result

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the Shift Value: "))
    ciphertext = caesar_cipher(plaintext, shift)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)

