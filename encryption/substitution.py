import random

def generate_substitution_key(base_key):
    """Generate a 256-character substitution key from the provided base key."""
    base_key = ''.join(dict.fromkeys(base_key))  # Remove duplicates while preserving order
    base_key = ''.join(c for c in base_key if ord(c) < 256)  # Filter to only ASCII characters

    if len(base_key) == 0:
        raise ValueError("Invalid key: Must contain at least one valid ASCII character.")

    ascii_chars = ''.join(chr(i) for i in range(256))
    remaining_chars = ''.join(c for c in ascii_chars if c not in base_key)

    # Shuffle remaining characters using a reproducible seed derived from base_key
    seed = sum(ord(c) for c in base_key)
    random.seed(seed)
    shuffled_remaining = list(remaining_chars)
    random.shuffle(shuffled_remaining)

    full_key = base_key + ''.join(shuffled_remaining)

    return full_key

def validate_substitution_key_input(base_key):
    """Validates that the base key has at least one valid ASCII character."""
    base_key = ''.join(c for c in base_key if ord(c) < 256)  # Filter to only ASCII characters
    if len(base_key) == 0:
        raise ValueError("Invalid key: Must contain at least one valid ASCII character.")

def substitution_encrypt(text, base_key):
    """Encrypt text using a substitution cipher with a generated key."""
    substitution_key = generate_substitution_key(base_key)  # Generate and validate key
    mapping = dict(zip(map(chr, range(256)), substitution_key))  # Create mapping
    return ''.join(mapping.get(char, char) for char in text)

def substitution_decrypt(text, base_key):
    """Decrypt text using a substitution cipher with a generated key."""
    substitution_key = generate_substitution_key(base_key)  # Generate and validate key
    reverse_mapping = {v: k for k, v in zip(map(chr, range(256)), substitution_key)}  # Create reverse mapping
    return ''.join(reverse_mapping.get(char, char) for char in text)


