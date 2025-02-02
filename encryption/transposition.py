import math

def validate_numeric_key(key):
    """Ensures the key contains only digits."""
    if not key.isdigit():
        raise ValueError("Invalid key: Transposition cipher requires a numeric key.")

def transposition_encrypt(text, key):
    validate_numeric_key(key)
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)
    
    grid = [''] * num_columns
    for index, char in enumerate(text):
        column = index % num_columns
        grid[column] += char

    return ''.join(grid)

def transposition_decrypt(text, key):
    validate_numeric_key(key)
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)

    extra_chars = len(text) % num_columns
    normal_col_length = len(text) // num_columns
    col_lengths = [normal_col_length + (1 if i < extra_chars else 0) for i in range(num_columns)]

    grid = []
    index = 0
    for length in col_lengths:
        grid.append(text[index:index + length])
        index += length

    decrypted_text = ""
    for i in range(num_rows):
        for col in range(num_columns):
            if i < len(grid[col]):
                decrypted_text += grid[col][i]

    return decrypted_text
