/* This is a generated file, see Makefile.am for its inputs. */
static const char machine_strings[] = "i386\0i486\0i586\0i686\0ppc\0ppc64\0ppc64le\0s390\0s390x\0x86_64";
static const unsigned machine_s2i_s[] = {
	0,5,10,15,20,24,30,38,43,49,
};
static const int machine_s2i_i[] = {
	0,0,0,0,4,3,10,6,5,1,
};
static int machine_s2i(const char *s, int *value) {
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
	return s2i__(machine_strings, machine_s2i_s, machine_s2i_i, 10, copy, value);
	}
}
static const unsigned machine_i2s_direct[] = {
	0,49,-1u,24,20,43,38,-1u,-1u,-1u,
	30,
};
static const char *machine_i2s(int v) {
	return i2s_direct__(machine_strings, machine_i2s_direct, 0, 10, v);
}
