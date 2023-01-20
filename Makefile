AS=riscv64-linux-gnu-as
CC=riscv64-linux-gnu-gcc
LD=riscv64-linux-gnu-ld
CFLAGS=-march=rv64idzk -static -O3 -Wall
AFLAGS=-march=rv64idzk

aes: aes.o aes_encrypt.o
	$(CC) $(CFLAGS) $^ -o $@

aes.o: aes.c
	$(CC) $(CFLAGS) -c $^

aes_encrypt.o: aes.S
	$(AS) $(AFLAGS) $^ -o $@

run: aes
	qemu-riscv64 -cpu rv64,zkne=true $^ 000102030405060708090a0b0c0d0e0f 101112131415161718191a1b1c1d1e1f

run-remote: aes
	qemu-riscv64 -g 1234 ./aes

setup:
	sudo pacman -S qemu-user riscv64-linux-gnu-gcc

clean:
	rm aes *.o