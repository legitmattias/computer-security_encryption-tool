import math
import threading

output_lock = threading.Lock()  # Global lock for synchronized logging & printing

def validate_transposition_key(ciphertext, key):
    """Ensures the key contains only digits, has no zeros, and does not exceed ciphertext length."""
    if not key.isdigit():
        raise ValueError(f"Invalid key ({key}): Transposition cipher requires a numeric key.")
    
    if '0' in key:
        raise ValueError(f"Invalid key ({key}): Transposition cipher keys cannot contain the digit '0'. Skipping.")

    if len(key) > len(ciphertext):
        raise ValueError(f"Invalid key ({key}): Key length ({len(key)}) exceeds ciphertext length ({len(ciphertext)}).")

    return key  # Keep the key unchanged

def build_transposition_grid(text, num_columns):
    """Creates a grid for transposition encryption."""
    num_rows = math.ceil(len(text) / num_columns)
    grid = ['' for _ in range(num_columns)]

    for index, char in enumerate(text):
        column = index % num_columns
        grid[column] += char

    return grid, num_rows

def transposition_encrypt(text, key):
    """Encrypt text using a transposition cipher where the key defines the column order."""
    key = validate_transposition_key(text, key)
    num_columns = len(key)

    grid, _ = build_transposition_grid(text, num_columns)

    # Determine the order of columns based on the key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    ordered_columns = [grid[idx] for idx, _ in key_order]

    return ''.join(ordered_columns)

def build_decryption_grid(ciphertext, key):
    """Builds the grid for decryption based on the key order."""
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)

    extra_chars = len(ciphertext) % num_columns
    normal_col_length = len(ciphertext) // num_columns
    col_lengths = [normal_col_length + (1 if i < extra_chars else 0) for i in range(num_columns)]

    # Determine the order of columns based on the key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    grid = [''] * num_columns
    index = 0
    for idx, _ in key_order:
        length = col_lengths[idx]
        grid[idx] = ciphertext[index:index + length]
        index += length

    return grid, num_rows

def transposition_decrypt(ciphertext, key):
    """Decrypt text using a transposition cipher where the key defines the column order."""
    key = validate_transposition_key(ciphertext, key)
    num_columns = len(key)

    grid, num_rows = build_decryption_grid(ciphertext, key)

    decrypted_text = ""
    for i in range(num_rows):
        for col in range(num_columns):
            if i < len(grid[col]):
                decrypted_text += grid[col][i]

    return decrypted_text

def brute_force_transposition(ciphertext, known_word, key):
    """Attempts transposition decryption with a given key."""
    try:
        decrypted_text = transposition_decrypt(ciphertext, key)
        if known_word in decrypted_text:
            with output_lock:  # 🔒 Lock output to prevent scrambling
                print(f"✅ Key Found: {key}")
                print(f"🔓 Decrypted Text:\n {decrypted_text}")
            return decrypted_text
    except ValueError as e:
        print(f"Skipping key {key}: {e}")  # Log invalid keys (not locked)
    except Exception:
        pass  # Ignore decryption errors

    return None
