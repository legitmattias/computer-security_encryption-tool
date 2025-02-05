import math

def validate_numeric_key(key):
    """Ensures the key contains only digits and removes duplicates."""
    if not key.isdigit():
        raise ValueError("Invalid key: Transposition cipher requires a numeric key.")
    key = ''.join(dict.fromkeys(key))  # Remove duplicate digits
    return key

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
    key = validate_numeric_key(key)
    num_columns = len(key)

    grid, _ = build_transposition_grid(text, num_columns)

    # Determine the order of columns based on the key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    ordered_columns = [grid[idx] for idx, _ in key_order]

    return ''.join(ordered_columns)

def build_decryption_grid(text, key):
    """Builds the grid for decryption based on the key order."""
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)

    extra_chars = len(text) % num_columns
    normal_col_length = len(text) // num_columns
    col_lengths = [normal_col_length + (1 if i < extra_chars else 0) for i in range(num_columns)]

    # Determine the order of columns based on the key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    grid = [''] * num_columns
    index = 0
    for idx, _ in key_order:
        length = col_lengths[idx]
        grid[idx] = text[index:index + length]
        index += length

    return grid, num_rows

def transposition_decrypt(text, key):
    """Decrypt text using a transposition cipher where the key defines the column order."""
    key = validate_numeric_key(key)
    num_columns = len(key)

    grid, num_rows = build_decryption_grid(text, key)

    decrypted_text = ""
    for i in range(num_rows):
        for col in range(num_columns):
            if i < len(grid[col]):
                decrypted_text += grid[col][i]

    return decrypted_text
