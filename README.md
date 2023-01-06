# Acceleration

## Description of the challenge
I implemented my encryption using the hardware acceleration. It is faster than I expected ! And you wil never recover the key !

Here is the [binary](challenge/aes) running on my server. If you don't have the correct hardware with you, you can run the encryption binary with qemu version 7.1.0 or later:

```bash
$ qemu-riscv64 -cpu rv64,zkne=true aes 2b7e151628aed2a6abf7158809cf4f3c 6bc1bee22e409f96e93d7e117393172a
7b771db8bac0ea40770d1b5b1314e443
```

## Installation

```bash
$ sudo systemctl start docker
$ docker build -t acceleration .
$ docker run -p:128:128 acceleration
```

The binary `challenge/aes` have to be shared with the participants but not the Python file `challenge/aes_encrypt.py`, it contains the flag.

# Solution

The program is a RISC-V 64-bit binary encrypting plaintext using the Cryptography extensions for AES called [Zkne](https://riscv.org/blog/2021/09/risc-v-cryptography-extensions-task-group-announces-public-review-of-the-scalar-cryptography-extensions/). Ghidra and radare2 does not disassemble those instructions properly yet. Thus, objdump should be used to figure out what the program is doing. A small modification have been done in the loop condition making the program to perform only one middle round instead of 9 for a standard AES. So the flaw is that the program is doing one middle round an one final round of AES which is a weak encryption. There is several way to recover the key from plaintexts and ciphertexts. I have chosen to use the tool [phoenixAES](https://github.com/SideChannelMarvels/JeanGrey) with one byte difference as plaintext input.
