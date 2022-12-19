/* sm4.c */
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <byteswap.h>

__uint128_t aes_round_encrypt(const uint64_t state0, uint64_t state1);

int main(int argc, char *argv[]) {
	char key_str[9] = {'\0'};
	char in_str[9] = {'\0'};
    uint64_t rk[16] = {0};
    //uint64_t out[2] = {0};
    uint64_t in[2] = {0};
	uint64_t key[2] = {0};

	__uint128_t out = 0;
	/*if (argc != 3) {
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

	strncpy(key_str, argv[1], 8);
	key[0] = bswap_32(strtoll(key_str, NULL, 16));
	strncpy(key_str, argv[1] + 8, 8);
	key[1] = bswap_32(strtoll(key_str, NULL, 16));
	strncpy(key_str, argv[1] + 16, 8);
	key[2] = bswap_32(strtoll(key_str, NULL, 16));
	strncpy(key_str, argv[1] + 24, 8);
	key[3] = bswap_32(strtoll(key_str, NULL, 16));
	
	// Copy plaintext
	strncpy(in_str, argv[2], 8);
	in[0] = strtol(in_str, NULL, 16);
	strncpy(in_str, argv[2] + 8, 8);
	in[1] = strtol(in_str, NULL, 16);
	strncpy(in_str, argv[2] + 16, 8);
	in[2] = strtol(in_str, NULL, 16);
	strncpy(in_str, argv[2] + 24, 8);
	in[3] = strtol(in_str, NULL, 16);*/

	//sm4_expand_key(key, rk, fk, ck);
	out = aes_round_encrypt(in[0], in[1]);
    printf("%032lx\n", out);
    return 0;
}
