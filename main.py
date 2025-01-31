import os
from encryption.substitution import substitution_encrypt, substitution_decrypt
from encryption.transposition import transposition_encrypt, transposition_decrypt

def main():
    print("Encryption/Decryption Program")
    mode = input("Do you want to encrypt (E) or decrypt (D)? ").strip().upper()
    method = input("Choose method - Substitution (S) or Transposition (T): ").strip().upper()
    
    file_name = input("Enter the name of the text file (inside `input/` folder): ").strip()
    key = input("Enter the secret key: ").strip()

    input_path = os.path.join("input", file_name)
    output_path = os.path.join("output", f"{file_name}.enc" if mode == "E" else f"{file_name}.dec")

    if not os.path.exists(input_path):
        print("Error: File not found!")
        return

    with open(input_path, "r") as file:
        text = file.read()

    if method == "S":
        result = substitution_encrypt(text, key) if mode == "E" else substitution_decrypt(text, key)
    elif method == "T":
        result = transposition_encrypt(text, key) if mode == "E" else transposition_decrypt(text, key)
    else:
        print("Invalid method selected.")
        return

    with open(output_path, "w") as file:
        file.write(result)

    print(f"Process complete. Output saved to: {output_path}")

if __name__ == "__main__":
    main()
