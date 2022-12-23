
.text
.global aes_encrypt, aes_expand_key

/*
 * void aes_expand_key(const uint64_t *key, uint64_t *rk);
*/
aes_expand_key:
	ld	t0, 0(a0)
	ld	t1, 8(a0)

	/* rk[0] */
	sd  t0, 0(a1)
	sd  t1, 8(a1)

	/* rk[1] */
	aes64ks1i t2, t1, 0
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 16(a1)
	sd  t1, 24(a1)

	/* rk[2] */
	aes64ks1i t2, t1, 1
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 32(a1)
	sd  t1, 40(a1)

	/* rk[3] */
	aes64ks1i t2, t1, 2
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 48(a1)
	sd  t1, 56(a1)

	/* rk[4] */
	aes64ks1i t2, t1, 3
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 64(a1)
	sd  t1, 72(a1)

	/* rk[5] */
	aes64ks1i t2, t1, 4
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 80(a1)
	sd  t1, 88(a1)

	/* rk[6] */
	aes64ks1i t2, t1, 5
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 96(a1)
	sd  t1, 104(a1)

	/* rk[7] */
	aes64ks1i t2, t1, 6
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 112(a1)
	sd  t1, 120(a1)

	/* rk[8] */
	aes64ks1i t2, t1, 7
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 128(a1)
	sd  t1, 136(a1)

	/* rk[9] */
	aes64ks1i t2, t1, 8
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 144(a1)
	sd  t1, 152(a1)

	/* rk[10] */
	aes64ks1i t2, t1, 9
	aes64ks2  t0, t2, t0
    aes64ks2  t1, t0, t1
	sd  t0, 160(a1)
	sd  t1, 168(a1)

	ret

/*
 * void aes_encrypt(const uint64_t *rk, uint64_t *plaintext, uint64_t *ciphertext);
*/
aes_encrypt:
	ld	t2, 0(a1)
	ld	t3, 8(a1)
	li	t4, 9
	mv 	t5, a0

	/* Add round key */
	ld	t0, 0(t5)
	ld	t1, 8(t5)
	addi t5, t5, 16
	xor	t2, t2, t0
	xor	t3, t3, t1

	loop:

	/* Rest of the round */
    aes64esm	t0, t2, t3
	aes64esm	t1, t3, t2
	
	/* Add round key */
	ld	t2, 0(t5)
	ld	t3, 8(t5)
	addi t5, t5, 16
	xor	t2, t2, t0
	xor	t3, t3, t1

	addi t4, t4, -1
	beq t4, zero, loop

	/* Final round */
	aes64es	t0, t2, t3
	aes64es	t1, t3, t2
	ld	t2, 0(t5)
	ld	t3, 8(t5)
	xor	t2, t2, t0
	xor	t3, t3, t1

	sd t2, 0(a2)
	sd t3, 8(a2)
	ret
