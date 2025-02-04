/* This is a generated file, see Makefile.am for its inputs. */
static const char seccomp_strings[] = "allow\0errno\0kill-process\0kill-thread\0log\0trace\0trap\0user-notify";
static const int seccomp_i2s_i[] = {
	-2147483648,0,196608,327680,2143289344,2146435072,2147221504,2147418112,
};
static const unsigned seccomp_i2s_s[] = {
	12,25,47,6,52,41,37,0,
};
static const char *seccomp_i2s(int v) {
	return i2s_bsearch__(seccomp_strings, seccomp_i2s_i, seccomp_i2s_s, 8, v);
}
