
.text
.global aes_round_encrypt, aes_expand_key

/*
 * uint64_t aes_expand_key(const uint64_t *key, uint64_t *rk);
*/
aes_expand_key:
	ld	t0, 0(a0)
	ld	t1, 8(a0)
	aes64ks1i t2, t1, 0
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	mv	a0, t2
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
