/* This is a generated file, see Makefile.am for its inputs. */
static const char uringop_strings[] = "accept\0close\0connect\0fallocate\0fgetxattr\0fsetxattr\0getxattr\0linkat\0mkdirat\0msg_ring\0"
	"openat\0openat2\0recvmsg\0renameat\0send_zc\0sendmsg\0sendmsg_zc\0setxattr\0shutdown\0symlinkat\0"
	"unlinkat\0uring_cmd";
static const unsigned uringop_s2i_s[] = {
	0,7,13,21,31,41,51,60,67,75,
	84,91,99,107,116,124,132,143,152,161,
	171,180,
};
static const int uringop_s2i_i[] = {
	13,19,16,17,43,41,44,39,37,40,
	18,28,10,35,47,9,48,42,34,38,
	36,46,
};
static int uringop_s2i(const char *s, int *value) {
	size_t len, i;
	 if (s == NULL || value == NULL)
		return 0;
	len = strlen(s);
	{ char copy[len + 1];
	for (i = 0; i < len; i++) {
		char c = s[i];
		copy[i] = GT_ISUPPER(c) ? c - 'A' + 'a' : c;
	}
	copy[i] = 0;
	return s2i__(uringop_strings, uringop_s2i_s, uringop_s2i_i, 22, copy, value);
	}
}
static const unsigned uringop_i2s_direct[] = {
	124,99,-1u,-1u,0,-1u,-1u,13,21,84,
	7,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,91,
	-1u,-1u,-1u,-1u,-1u,152,107,171,67,161,
	60,75,41,143,31,51,-1u,180,116,132,
};
static const char *uringop_i2s(int v) {
	return i2s_direct__(uringop_strings, uringop_i2s_direct, 9, 48, v);
}
