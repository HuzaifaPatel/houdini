/* This is a generated file, see Makefile.am for its inputs. */
static const char normalize_syscall_map_strings[] = "accept\0accept4\0access\0adjtimex\0bind\0brk\0chmod\0chown\0clock_settime\0connect\0"
	"creat\0delete_module\0execve\0execveat\0faccessat\0faccessat2\0fallocate\0fchmod\0fchmodat\0fchown\0"
	"fchownat\0finit_module\0fremovexattr\0fsetxattr\0fsmount\0fspick\0fstat\0fstatfs\0ftruncate\0futimesat\0"
	"init_module\0kill\0lchown\0lremovexattr\0lsetxattr\0lstat\0memfd_create\0mkdir\0mkdirat\0mknod\0"
	"mknodat\0mmap\0mount\0move_mount\0newfstatat\0open\0openat\0openat2\0readlink\0readlinkat\0"
	"recvfrom\0recvmsg\0removexattr\0rename\0renameat\0renameat2\0rmdir\0sched_setattr\0sched_setparam\0sched_setscheduler\0"
	"sendmsg\0sendto\0setdomainname\0setegid\0seteuid\0setfsgid\0setfsuid\0setgid\0sethostname\0setregid\0"
	"setresgid\0setresuid\0setreuid\0settimeofday\0setuid\0setxattr\0stat\0stat64\0statfs\0statx\0"
	"stime\0symlink\0symlinkat\0tgkill\0tkill\0truncate\0umount\0umount2\0unlink\0unlinkat\0"
	"utime\0utimensat\0utimes";
static const unsigned normalize_syscall_map_s2i_s[] = {
	0,7,15,22,31,36,40,46,52,66,
	74,80,94,101,110,120,131,141,148,157,
	164,173,186,199,209,217,224,230,238,248,
	258,270,275,282,295,305,311,324,330,338,
	344,352,357,363,374,385,390,397,405,414,
	425,434,442,454,461,470,480,486,500,515,
	534,542,549,563,571,579,588,597,604,616,
	625,635,645,654,667,674,683,688,695,702,
	708,714,722,732,739,745,754,761,769,776,
	785,791,801,
};
static const int normalize_syscall_map_s2i_i[] = {
	16,16,10,31,17,35,3,4,31,18,
	1,6,15,15,10,10,1,3,3,4,
	4,5,2,2,8,8,10,34,1,14,
	5,21,4,2,2,10,1,7,7,32,
	32,35,8,8,10,1,1,1,1,1,
	19,19,2,9,9,9,13,36,36,36,
	20,20,33,30,29,30,29,30,33,30,
	30,29,29,31,29,2,10,10,34,10,
	31,11,11,21,21,1,12,12,13,13,
	14,14,14,
};
static int normalize_syscall_map_s2i(const char *s, int *value) {
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
	return s2i__(normalize_syscall_map_strings, normalize_syscall_map_s2i_s, normalize_syscall_map_s2i_i, 93, copy, value);
	}
}
