print('<-------------------Pixel Manipulation for Image Encryption------------------->')
from PIL import Image # type: ignore

def shift_pixel_value(value, shift):
    """ Shift the pixel value with wrapping. """
    return (value + shift) % 256

def encrypt_image(input_path, output_path, shift):
    """ Encrypt the image by shifting pixel RGB values. """
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()  # Load pixel data

    # Get image dimensions
    width, height = img.size

    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt each RGB component
            r_encrypted = shift_pixel_value(r, shift)
            g_encrypted = shift_pixel_value(g, shift)
            b_encrypted = shift_pixel_value(b, shift)

            # Set the new pixel value
            pixels[x, y] = (r_encrypted, g_encrypted, b_encrypted)

    # Save the encrypted image
    img.save(output_path)

def decrypt_image(input_path, output_path, shift):
    """ Decrypt the image by reversing the shift on pixel RGB values. """
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()  # Load pixel data

    # Get image dimensions
    width, height = img.size

    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Decrypt each RGB component
            r_decrypted = shift_pixel_value(r, -shift)
            g_decrypted = shift_pixel_value(g, -shift)
            b_decrypted = shift_pixel_value(b, -shift)

            # Set the new pixel value
            pixels[x, y] = (r_decrypted, g_decrypted, b_decrypted)

    # Save the decrypted image
    img.save(output_path)

if __name__ == "__main__":
    input_image_path = "input_image.png"
    encrypted_image_path = "encrypted_image.png"
    decrypted_image_path = "decrypted_image.png"
    
    shift_value1 = int(input("Enter Shift value for Encryption: "))  # pixel shift value for Encryption
    encrypt_image(input_image_path, encrypted_image_path, shift_value1)
    print(f"Image encrypted and saved as {encrypted_image_path}")
    
    shift_value2 = int(input("Enter Shift value for Decryption: "))  # pixel shift value for Decryption
    decrypt_image(encrypted_image_path, decrypted_image_path, shift_value2)
    print(f"Image decrypted and saved as {decrypted_image_path}")
