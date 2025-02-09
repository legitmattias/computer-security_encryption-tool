# Encryption Tool & Brute-Force Scripts

This repository contains an encryption and decryption tool developed as part of a university assignment, along with custom brute-force scripts designed to analyze and break transposition ciphers. **No external cryptographic libraries were allowed** for the encryption implementation, so all algorithms were built from scratch.

## Features

- **Substitution Cipher** (Basic encryption/decryption)
- **Transposition Cipher** (Standard columnar transposition encryption/decryption)
- **Brute-force Transposition Decryption** (Custom scripts to attempt decryption by trying all possible keys)
- **Multi-threading & Multi-processing Support** for improved performance

## Repository Structure

```
 encryption_tool/
 ├── encryption/
 │   ├── __init__.py
 │   ├── substitution.py          # Substitution cipher implementation
 │   ├── transposition_mt.py      # Multi-threaded transposition cipher implementation
 │   ├── transposition_mp.py      # Multi-processing transposition cipher implementation
 │
 ├── brute_force_transposition_script_mt.py  # Multi-threaded brute-force decryption script
 ├── brute_force_transposition_script_mp.py  # Multi-processing brute-force decryption script
 │
 ├── config.py                     # Configuration settings
 ├── main.py                        # Main script for encryption/decryption
 ├── manual_test.py                 # Manual testing script
 │
 ├── .gitignore                     # Git ignore file
```

## Encryption & Decryption

The encryption tool supports **substitution** and **transposition** ciphers. Since no cryptographic libraries were permitted, all algorithms were manually implemented.

### Usage:

Run the main script to encrypt or decrypt text files:

```sh
python main.py
```

Follow the on-screen prompts to choose:
- Encryption (E) / Decryption (D)
- Cipher Method: Substitution (S) or Transposition (T)
- Input file
- Key

The output will be saved in the `output/` directory.

## Brute-Force Decryption

The brute-force scripts attempt to decrypt **transposition ciphers** by testing different key permutations.

### Multi-Threaded Version:
```sh
python brute_force_transposition_script_mt.py <folder_path> <known_word> [max_key_length] [--no-show]
```

### Multi-Processing Version:
```sh
python brute_force_transposition_script_mp.py <folder_path> <known_word> [max_key_length] [--no-show]
```

#### Parameters:
- `<folder_path>`: Path to the folder containing cipher text files
- `<known_word>`: A word that is expected to be in the decrypted text
- `[max_key_length]`: (Optional) Maximum length of the transposition key (default: 6, max: 9)
- `--no-show`: (Optional) If included, prevents decrypted text from being printed to the terminal

### Output:
- A log file is generated in `logs/`, containing results and statistics.
- Successfully decrypted files are stored in a timestamped folder.

## Performance Optimization

Since brute-forcing transposition ciphers is computationally expensive, **multi-threading** and **multi-processing** implementations were added to speed up execution.

- **Multi-threading (`mt`)**: Best suited for I/O-bound operations
- **Multi-processing (`mp`)**: Utilizes all CPU cores for faster brute-force attempts

## Disclaimer

This tool was created for educational purposes and **should not be used for unauthorized decryption or security breaches**. Always ensure you have permission before attempting to break encryption.
