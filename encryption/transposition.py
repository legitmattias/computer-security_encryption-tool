import math

def transposition_encrypt(text, key):
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)
    grid = [''] * num_columns

    for index, char in enumerate(text):
        column = index % num_columns
        grid[column] += char

    return ''.join(grid)

def transposition_decrypt(text, key):
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)
    
    num_full_cols = len(text) % num_columns
    grid = [''] * num_columns
    col, row = 0, 0

    for char in text:
        grid[col] += char
        col += 1
        if col == num_columns or (col == num_full_cols and row >= num_rows - 1):
            col, row = 0, row + 1

    return ''.join(grid)
