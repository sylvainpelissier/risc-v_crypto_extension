/* sm4.c */
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <byteswap.h>

uint64_t aes_round_encrypt(const uint64_t state0, uint64_t state1);
uint64_t aes_expand_key(const uint64_t *key, uint64_t *rk);

int main(int argc, char *argv[]) {
	char key_str[17] = {'\0'};
	char in_str[17] = {'\0'};
    uint64_t rk[16] = {0};
    uint64_t out[2] = {0};
    uint64_t in[2] = {0};
	uint64_t key[2] = {0};

	if (argc != 3) {
		printf("Usage: ./sm4 <key> <plaintext>\n");
		return 1;
	}
	if (strlen(argv[1]) != 32) {
		printf("Key should be 16-byte long in hexadecimal.\n");
		return 1;
	}
	if (strlen(argv[2]) != 32) {
		printf("Plaintext should be 16-byte long in hexadecimal.\n");
		return 1;
	}
    
	// Copy key
	strncpy(key_str, argv[1], 16);
	key[0] = strtoull(key_str, NULL, 16);
	strncpy(key_str, argv[1] + 16, 16);
	key[1] = strtoull(key_str, NULL, 16);
	printf("%016lx%016lx\n", key[0], key[1]);
	
	out[0] = aes_expand_key(key, rk);
	printf("%016lx\n", out[0]);
	
	// Copy plaintext
	strncpy(in_str, argv[2], 16);
	in[0] = strtoull(in_str, NULL, 16);
	strncpy(in_str, argv[2] + 16, 16);
	in[1] = strtoull(in_str, NULL, 16);
	printf("%016lx%016lx\n", in[0], in[1]);

	out[0] = aes_round_encrypt(in[0], in[1]);
    printf("%016lx\n", out[0]);
    return 0;
}
