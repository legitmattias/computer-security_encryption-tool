import string

def create_substitution_key(key):
    alphabet = string.ascii_uppercase
    key = (key * (len(alphabet) // len(key) + 1))[:len(alphabet)]  # Repeat key
    mapping = dict(zip(alphabet, key.upper()))
    reverse_mapping = {v: k for k, v in mapping.items()}
    return mapping, reverse_mapping

def substitution_encrypt(text, key):
    mapping, _ = create_substitution_key(key)
    return ''.join(mapping.get(char.upper(), char) for char in text)

def substitution_decrypt(text, key):
    _, reverse_mapping = create_substitution_key(key)
    return ''.join(reverse_mapping.get(char.upper(), char) for char in text)
