
.text
.global aes_round_encrypt, aes_expand_key

/*
 * void sm4_expand_key(const u32 *rk, u32 *out, const u32 *in);
*/
aes_expand_key:
	ret

/*
 * uint64_t aes_encrypt(const uint64_t state0, uint64_t state1);
*/
aes_round_encrypt:
    aes64esm	t1, a0, a1
	aes64esm	t2, a1, a0
	mv			a0, t1
	mv			a1, t2
	ret
