from encryption.substitution import (
    substitution_encrypt,
    substitution_decrypt,
    generate_substitution_key,
    validate_substitution_key_input,
)
from encryption.transposition_mt import (
    transposition_encrypt,
    transposition_decrypt,
    validate_transposition_key,
)

# Test data
text = "test message"
sub_key_valid = "qwerty"
sub_key_invalid = "😇😇😇😇"
trans_key_valid = "132"
trans_key_invalid = "12a3"

# Test 1: Valid Substitution Key Encryption/Decryption
try:
    validate_substitution_key_input(sub_key_valid)
    full_sub_key = generate_substitution_key(sub_key_valid)
    enc_sub = substitution_encrypt(text, sub_key_valid)
    dec_sub = substitution_decrypt(enc_sub, sub_key_valid)
    assert dec_sub == text, "Substitution decryption failed with valid key."
    print("Test 1 Passed: Substitution encryption/decryption with valid key.")
except Exception as e:
    print(f"Test 1 Failed: {e}")

# Test 2: Invalid Substitution Key
try:
    validate_substitution_key_input(sub_key_invalid)
    print("Test 2 Failed: Invalid substitution key was not rejected.")
except ValueError as _:
    print("Test 2 Passed: Invalid substitution key correctly rejected.")

# Test 3: Valid Transposition Key Encryption/Decryption
try:
    validate_transposition_key(text, trans_key_valid)
    enc_trans = transposition_encrypt(text, trans_key_valid)
    dec_trans = transposition_decrypt(enc_trans, trans_key_valid)
    assert dec_trans == text, "Transposition decryption failed with valid key."
    print("Test 3 Passed: Transposition encryption/decryption with valid key.")
except Exception as e:
    print(f"Test 3 Failed: {e}")

# Test 4: Invalid Transposition Key
try:
    validate_transposition_key(text, trans_key_invalid)
    print("Test 4 Failed: Invalid transposition key was not rejected.")
except ValueError as _:
    print("Test 4 Passed: Invalid transposition key correctly rejected.")

# Test 5: Edge Case - Empty Text Encryption/Decryption
try:
    # Substitution Cipher Test with Empty Text
    try:
        enc_empty_sub = substitution_encrypt("", sub_key_valid)
        dec_empty_sub = substitution_decrypt(enc_empty_sub, sub_key_valid)
        assert dec_empty_sub == "", "Substitution decryption failed with empty text."
        print("Test 5 Passed: Encryption/decryption works correctly with empty text (Substitution).")
    except Exception as e:
        print(f"Test 5 Failed: {e} (Substitution) ")

    # Transposition Cipher Test with Empty Text
    try:
        enc_empty_trans = transposition_encrypt("", trans_key_valid)
        dec_empty_trans = transposition_decrypt(enc_empty_trans, trans_key_valid)
        assert dec_empty_trans == "", "Transposition decryption should fail with empty text."
        print("Test 5 Failed: Encryption/decryption should not work with empty text (Transposition).")
    except Exception as e:
        print(f"Test 5 Passed: Properly failed with empty text - {e} (Transposition) ")

except Exception as e:
    print(f"Test 5 Unexpected Failure: {e}")

# Test 6: Edge Case - Single Character Encryption/Decryption
try:
    # Substitution Cipher Test with Single Character
    try:
        enc_single_sub = substitution_encrypt("A", sub_key_valid)
        dec_single_sub = substitution_decrypt(enc_single_sub, sub_key_valid)
        assert dec_single_sub == "A", "Substitution decryption failed with single character."
        print("Test 6 Passed: Encryption/decryption works correctly with single character (Substitution).")
    except Exception as e:
        print(f"Test 6 Failed: {e} (Substitution) ")

    # Transposition Cipher Test with Single Character
    try:
        enc_single_trans = transposition_encrypt("A", trans_key_valid)
        dec_single_trans = transposition_decrypt(enc_single_trans, trans_key_valid)
        assert dec_single_trans == "A", "Transposition decryption should have failed with single character."
        print("Test 6 Failed: Encryption/decryption should not work with single character (Transposition).")
    except Exception as e:
        print(f"Test 6 Passed: Properly failed with single character - {e} (Transposition)")


except Exception as e:
    print(f"Test 6 Unexpected Failure: {e}")
