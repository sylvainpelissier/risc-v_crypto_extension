AS=riscv64-linux-gnu-as
CC=riscv64-linux-gnu-gcc
LD=riscv64-linux-gnu-ld
CFLAGS=-march=rv64ifdczk -static -O3
AFLAGS=-march=rv64ifdczk

aes: aes.o aes_encrypt.o
	$(CC) $(CFLAGS) $^ -o $@

aes.o: aes.c
	$(CC) $(CFLAGS) -c $^

aes_encrypt.o: aes.S
	$(AS) $(AFLAGS) $^ -o $@

run: aes
	qemu-riscv64 -cpu rv64,zkne=true $^

run-remote: aes
	qemu-riscv64 -g 1234 ./aes

setup:
	sudo pacman -S qemu-user riscv64-linux-gnu-gcc

clean:
	rm aes *.o