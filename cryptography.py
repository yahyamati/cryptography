from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key, output_path):
    # Ensure the key is an integer
    try:
        key = int(key)
    except ValueError:
        print("The key must be an integer.")
        return
    
    if not (0 <= key <= 255):
        print("The key must be between 0 and 255.")
        return

    # Load the image
    try:
        image = Image.open(image_path)  # Open the image
    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")
        return
    
    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Encrypt the image using the XOR operation
    encrypt_array = image_array ^ key  # XOR operation with the key

    # Convert the NumPy array back to an image
    encrypt_image = Image.fromarray(encrypt_array)

    # Save the encrypted image
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    encrypt_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(encrypted_path, key, output_path):
    # Ensure the key is an integer
    try:
        key = int(key)
    except ValueError:
        print("The key must be an integer.")
        return
    
    if not (0 <= key <= 255):
        print("The key must be between 0 and 255.")
        return

    # Load the encrypted image
    try:
        encrypted_image = Image.open(encrypted_path)  # Open the encrypted image
    except FileNotFoundError:
        print(f"Image file '{encrypted_path}' not found.")
        return
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_image)
    
    # Ensure that the data type is correctly handled
    decrypted_array = (encrypted_array ^ key).astype(np.uint8)  # XOR operation with the key and convert back to uint8

    # Convert the NumPy array back to an image
    decrypted_image = Image.fromarray(decrypted_array)
    
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


# Main logic for user input and action
choice = input("Enter '0' to encrypt an image: or '1' to decrypt an image ")

if choice == "1":
    # Decryption process
    encrypted_path = input("Enter the encrypted image path: ")
    key = input("Enter your decryption key (0-255): ")
    output_path = input("Enter the output path for the decrypted image: ")
    decrypt_image(encrypted_path, key, output_path)

elif choice == "0":
    # Encryption process
    image_path = input("Enter the original image path: ")
    key = input("Enter your encryption key (0-255): ")
    output_path = input("Enter the output path for the encrypted image: ")
    encrypt_image(image_path, key, output_path)

else:
    print("Invalid choice. Please enter '1' for decryption or '0' for encryption.")
