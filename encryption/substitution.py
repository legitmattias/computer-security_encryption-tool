import random
import string

PRINTABLE_CHARS = ''.join(chr(i) for i in range(32, 127))

def generate_substitution_key(base_key):
    """Generate a substitution key for printable ASCII characters."""
    base_key = clean_key(base_key)

    if len(base_key) == 0:
        raise ValueError("Invalid key: Must contain at least one printable ASCII character.")

    remaining_chars = ''.join(c for c in PRINTABLE_CHARS if c not in base_key)

    # Shuffle remaining characters using a reproducible seed derived from base_key
    seed = sum(ord(c) for c in base_key)
    random.seed(seed)
    shuffled_remaining = list(remaining_chars)
    random.shuffle(shuffled_remaining)

    # Combine base_key with the shuffled remaining characters
    full_key = base_key + ''.join(shuffled_remaining)

    return full_key

def clean_key(base_key):
    """Remove duplicates and filter to printable ASCII characters."""
    base_key = ''.join(dict.fromkeys(base_key))  # Remove duplicates
    return ''.join(c for c in base_key if c in string.printable and c not in string.whitespace)

def validate_substitution_key_input(base_key):
    """Validate that the base key has at least one printable ASCII character."""
    base_key = clean_key(base_key)
    if len(base_key) == 0:
        raise ValueError("Invalid key: Must contain at least one printable ASCII character.")

def create_mapping(substitution_key):
    """Create mapping for encryption and decryption."""
    mapping = dict(zip(PRINTABLE_CHARS, substitution_key))
    reverse_mapping = {v: k for k, v in mapping.items()}
    return mapping, reverse_mapping

def substitution_encrypt(text, base_key):
    """Encrypt text using a substitution cipher with printable characters."""
    substitution_key = generate_substitution_key(base_key)
    mapping, _ = create_mapping(substitution_key)
    
    # Encrypt printable characters; leave non-printable characters unchanged
    return ''.join(mapping.get(char, char) for char in text)

def substitution_decrypt(text, base_key):
    """Decrypt text using a substitution cipher with printable characters."""
    substitution_key = generate_substitution_key(base_key)
    _, reverse_mapping = create_mapping(substitution_key)

    # Decrypt printable characters; leave non-printable characters unchanged
    return ''.join(reverse_mapping.get(char, char) for char in text)
