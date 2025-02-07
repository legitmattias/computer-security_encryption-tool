import os
from encryption.substitution import substitution_encrypt, substitution_decrypt, validate_substitution_key_input
from encryption.transposition_mt import transposition_encrypt, transposition_decrypt, validate_transposition_key

def get_mode():
    """Get encryption/decryption mode from the user."""
    while True:
        mode = input("Do you want to encrypt (E) or decrypt (D)? ").strip().upper()
        if mode in ["E", "D"]:
            return mode
        else:
            print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

def get_method():
    """Get cipher method from the user."""
    while True:
        method = input("Choose method - Substitution (S) or Transposition (T): ").strip().upper()
        if method in ["S", "T"]:
            return method
        else:
            print("Invalid choice. Please enter 'S' for substitution or 'T' for transposition.")

def get_file_name():
    """Get file name from the user and ensure it exists."""
    while True:
        file_name = input("Enter the name of the text file (inside `input/` folder): ").strip()
        input_path = os.path.join("input", file_name)
        if os.path.exists(input_path):
            return file_name, input_path
        else:
            print("Error: File not found. Please enter a valid file name.")

def get_key(text, method):
    """Get and validate key based on method."""
    while True:
        key = input("Enter the secret key: ").strip()
        try:
            if method == "S":
                validate_substitution_key_input(key)
            elif method == "T":
                validate_transposition_key(text, key)
            return key
        except ValueError as e:
            print(e)

def main():
    print("Encryption/Decryption Program")

    mode = get_mode()
    method = get_method()
    file_name, input_path = get_file_name()
    
    # Read the content from the input file with latin1 encoding
    with open(input_path, "r", encoding='latin1') as file:
        text = file.read()
    
    key = get_key(text, method)


    # Perform encryption or decryption
    if method == "S":
        result = substitution_encrypt(text, key) if mode == "E" else substitution_decrypt(text, key)
    elif method == "T":
        result = transposition_encrypt(text, key) if mode == "E" else transposition_decrypt(text, key)

    # Save the output file with latin1 encoding
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    output_path = os.path.join(output_dir, f"{file_name}.enc" if mode == "E" else f"{file_name}.dec")
    with open(output_path, "w", encoding='latin1') as file:
        file.write(result)

    print(f"Process complete. Output saved to: {output_path}")

if __name__ == "__main__":
    main()