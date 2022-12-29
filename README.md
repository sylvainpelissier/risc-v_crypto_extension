# RISC-V Cryptography extension

## Description
I implemented my encryption using the hardware acceleration. It is faster than I expected ! And you wil never recover the key !

Here is the [binary](challenge/aes). If you don't have the hardware with you, you can run the encryption binary with qemu version 7.1.0 or later:

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
