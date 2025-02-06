import os
import sys
import itertools
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import threading

from encryption.transposition import brute_force_transposition

output_lock = threading.Lock()  # Global lock for synchronized logging & printing

def generate_priority_keys():
    """Generate a list of key combinations to try first based on common patterns."""
    priority_keys = [
        # Simple sequences with unique digits
        123, 1234, 12345, 123456, 1234567, 12345678, 12345689, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321, 15973, 35791, 97431, 987654, 13579, 8642,
    ]

    # Generate years from 1900 to 1999, excluding any that contain '0'
    for year in range(1900, 2000):
        if "0" not in str(year):
            priority_keys.append(year)
    return priority_keys

def process_file(filename, folder_path, known_word, max_key_length, log_filename):
    """Processes a single file for decryption."""
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='latin1') as file:
        ciphertext = file.read()

    start_time = time.time()
    
    thread_name = threading.current_thread().name
    with output_lock:
      print(f"🔍 Attempting to decrypt: {filename}. Assigned to 🤖 {thread_name}.")

    result = None

    # Try priority keys first
    for key in generate_priority_keys():
        result = brute_force_transposition(ciphertext, known_word, str(key))
        if result:
            break

    # If not found, proceed with full brute-force
    if not result:
        for key_length in range(2, max_key_length + 1):  # Generate keys of increasing length
            for perm in itertools.permutations(range(1, key_length + 1)):  # Unique digits 1-9
                key = ''.join(map(str, perm))
                result = brute_force_transposition(ciphertext, known_word, key)
                if result:
                    break
            if result:
                break

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Log results
    with output_lock:
      with open(log_filename, 'a') as log_file:
        if result:
            print(f"✅ Decryption successful for file: {filename} (Time: {elapsed_time:.2f} seconds)")
            log_file.write(f"✅ Decryption successful for file: {filename} (Time: {elapsed_time:.2f} seconds)\n")
        else:
            print(f"❌ No key found for file: {filename} (Time: {elapsed_time:.2f} seconds)")
            log_file.write(f"❌ No key found for file: {filename} (Time: {elapsed_time:.2f} seconds)\n")


def search_folder_for_ciphers(folder_path, known_word, max_key_length=6):
    """Runs decryption in parallel using multiple CPU threads with dynamic scheduling."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_filename = os.path.join(log_dir, f"transposition_decryption_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    total_start_time = time.time()

    # Write title and summary to terminal (stdout)
    print("=== Transposition Cipher Brute-Force ===\n")
    print(f"Folder: {folder_path}\n")
    print(f"Keyword: {known_word}\n")
    print(f"Max Key Length: {max_key_length}\n")
    print("=======================================\n\n")

    # Write log title and summary
    with open(log_filename, 'w') as log_file:
        log_file.write("=== Transposition Cipher Brute-Force Log ===\n")
        log_file.write(f"Folder: {folder_path}\n")
        log_file.write(f"Keyword: {known_word}\n")
        log_file.write(f"Max Key Length: {max_key_length}\n")
        log_file.write("=======================================\n\n")

    # Dynamically assign work with 'submit()'
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for filename in files:
            futures.append(executor.submit(process_file, filename, folder_path, known_word, max_key_length, log_filename))

        # Ensure all tasks complete before continuing
        for future in futures:
            future.result()

    total_end_time = time.time()
    total_elapsed_time = total_end_time - total_start_time

    # Log total time
    with open(log_filename, 'a') as log_file:
        print(f"⏱️ Total brute-force time: {total_elapsed_time:.2f} seconds")
        log_file.write(f"⏱️ Total brute-force time: {total_elapsed_time:.2f} seconds\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python brute_force_script.py <folder_path> <known_word> [max_key_length]")
        sys.exit(1)

    folder_path = sys.argv[1]
    known_word = sys.argv[2]
    max_key_length = int(sys.argv[3]) if len(sys.argv) > 3 else 6

    # Sanitize max_key_length (should be between 2 and 9)
    if not (2 <= max_key_length <= 9):
        print(f"Invalid max_key_length: {max_key_length}. It must be between 2 and 9 (since 0 is not allowed in transposition keys).")
        sys.exit(1)

    search_folder_for_ciphers(folder_path, known_word, max_key_length)
