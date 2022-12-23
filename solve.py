import os
import phoenixAES

from  risc-v_crypto_extension.challenge.aes_encrypt import encrypt
from binascii import unhexlify
from aeskeyschedule import reverse_key_schedule

if __name__ == "__main__":
    key = b"INS{AeS_2r0Und5}"
    print(key.hex())
    # Generate differences
    plaintext = [0 for _ in range(16)]
    ref = encrypt(key, plaintext)
    ciphertexts = []

    for b in range(4):
        for i in range(1,9,7):
            plaintext = [0 for _ in range(16)]
            plaintext[b] = i
            plaintext = bytes(plaintext)
            ciphertext = encrypt(key, plaintext)
            ciphertexts.append(ciphertext)
    
    key = unhexlify(phoenixAES.crack_bytes(ciphertexts, ref))
    print(reverse_key_schedule(key, 2))