import os
import sys
import time
from datetime import datetime
from encryption.transposition import brute_force_transposition

def search_folder_for_ciphers(folder_path, known_word, max_key_length=6):
    log_filename = f"transposition_decryption_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(log_filename, 'w') as log_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='latin1') as file:
                    ciphertext = file.read()

                print(f"Attempting to decrypt: {filename}")
                start_time = time.time()
                result = brute_force_transposition(ciphertext, known_word, max_key_length)
                end_time = time.time()
                elapsed_time = end_time - start_time

                if result:
                    print(f"✅ Decryption successful for file: {filename} (Time: {elapsed_time:.2f} seconds)")
                    log_file.write(f"✅ Decryption successful for file: {filename} (Time: {elapsed_time:.2f} seconds)\n")
                else:
                    print(f"❌ No key found for file: {filename} (Time: {elapsed_time:.2f} seconds)")
                    log_file.write(f"❌ No key found for file: {filename} (Time: {elapsed_time:.2f} seconds)\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python brute_force_script.py <folder_path> <known_word> [max_key_length]")
        sys.exit(1)

    folder_path = sys.argv[1]
    known_word = sys.argv[2]
    max_key_length = int(sys.argv[3]) if len(sys.argv) > 3 else 6

    search_folder_for_ciphers(folder_path, known_word, max_key_length)
