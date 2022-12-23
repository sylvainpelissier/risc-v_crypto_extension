import phoenixAES
import telnetlib

HOST = "127.0.0.1"
PORT = 128

from binascii import unhexlify
from aeskeyschedule import reverse_key_schedule

if __name__ == "__main__":
    
    tn = telnetlib.Telnet(HOST, PORT)

    rsp = tn.read_until(b"Enter the plaintext:")

    # Generate differences
    plaintext = b"\x00"*16
    tn.write(plaintext.hex().encode() + b"\n")
    rsp = tn.read_until(b"\n")
    ref = unhexlify(rsp.split(b"\n")[0][-32:])
    print(f"Got reference: {ref}")

    ciphertexts = []
    for b in range(4):
        for i in range(1,9,7):
            rsp = tn.read_until(b"Enter the plaintext:")
            plaintext = [0 for _ in range(16)]
            plaintext[b] = i
            plaintext = bytes(plaintext)
            tn.write(plaintext.hex().encode() + b"\n")
            rsp = tn.read_until(b"\n")
            ciphertext = unhexlify(rsp.split(b"\n")[0][-32:])
            ciphertexts.append(ciphertext)
            print(f"Got ciphertext: {ciphertext}")
    
    key = unhexlify(phoenixAES.crack_bytes(ciphertexts, ref))
    print(reverse_key_schedule(key, 2))