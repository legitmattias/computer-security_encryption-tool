import os
from encryption.substitution import substitution_encrypt, substitution_decrypt, validate_substitution_key_input
from encryption.transposition import transposition_encrypt, transposition_decrypt, validate_numeric_key

def main():
    print("Encryption/Decryption Program")

    # Get encryption/decryption mode
    while True:
        mode = input("Do you want to encrypt (E) or decrypt (D)? ").strip().upper()
        if mode in ["E", "D"]:
            break
        else:
            print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

    # Get cipher method
    while True:
        method = input("Choose method - Substitution (S) or Transposition (T): ").strip().upper()
        if method in ["S", "T"]:
            break
        else:
            print("Invalid choice. Please enter 'S' for substitution or 'T' for transposition.")

    # Get file name and ensure it exists
    while True:
        file_name = input("Enter the name of the text file (inside `input/` folder): ").strip()
        input_path = os.path.join("input", file_name)
        if os.path.exists(input_path):
            break
        else:
            print("Error: File not found. Please enter a valid file name.")

    # Get and validate key based on method
    while True:
        key = input("Enter the secret key: ").strip()
        try:
            if method == "S":
                validate_substitution_key_input(key)
            elif method == "T":
                validate_numeric_key(key)
            break  # Exit loop if key is valid
        except ValueError as e:
            print(e)  # Show validation error and prompt again

    # Read the content from the input file
    with open(input_path, "r") as file:
        text = file.read()

    # Perform encryption or decryption
    if method == "S":
        result = substitution_encrypt(text, key) if mode == "E" else substitution_decrypt(text, key)
    elif method == "T":
        result = transposition_encrypt(text, key) if mode == "E" else transposition_decrypt(text, key)

    # Save the output file
    output_path = os.path.join("output", f"{file_name}.enc" if mode == "E" else f"{file_name}.dec")
    with open(output_path, "w") as file:
        file.write(result)

    print(f"Process complete. Output saved to: {output_path}")

if __name__ == "__main__":
    main()
