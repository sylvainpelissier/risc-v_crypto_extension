from matrix import matrix2bytes
from sbox import sub_bytes, s_box
from diffusion import mix_columns, shift_rows
from add_round_key import add_round_key
from binascii import unhexlify

N_ROUNDS = 10

"""
key        = unhexlify(b'2b7e151628aed2a6abf7158809cf4f3c')
ciphertext = unhexlify(b'3ad77bb40d7a3660a89ecaf32466ef97')
plaintext = unhexlify(b'6bc1bee22e409f96e93d7e117393172a')
"""

key        = unhexlify(b'000102030405060708090a0b0c0d0e0f')
ciphertext = unhexlify(b'11111111111111111111111111111111')
plaintext = unhexlify(b'101112131415161718191a1b1c1d1e1f')

def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def encrypt(key, ciphertext):
    round_keys = expand_key(key) # Remember to start from the last round key and work backwards through them when decrypting

    # Convert ciphertext to state matrix
    state = bytes2matrix(ciphertext)

    # Initial add round key step
    state = add_round_key(state, round_keys[0])

    for i in range(1, N_ROUNDS):
        # subBytes
        state = sub_bytes(state)

        # shift row
        shift_rows(state)

        # mix column
        mix_columns(state)

        # Add round key step
        state = add_round_key(state, round_keys[i])

        print(matrix2bytes(state).hex())

        

    # Run final round (skips the InvMixColumns step)
    state = sub_bytes(state, sbox=s_box)
    shift_rows(state)
    state = add_round_key(state, round_keys[N_ROUNDS])

    # Convert state matrix to plaintext
    plaintext = matrix2bytes(state)
    print(plaintext.hex())
    return plaintext


print(encrypt(key, plaintext).hex())
assert ciphertext == encrypt(key, plaintext)
