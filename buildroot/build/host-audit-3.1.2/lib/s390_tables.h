/* This is a generated file, see Makefile.am for its inputs. */
static const char s390_syscall_strings[] = "_llseek\0_newselect\0_sysctl\0accept4\0access\0acct\0add_key\0adjtimex\0afs_syscall\0alarm\0"
	"bdflush\0bind\0bpf\0brk\0cachestat\0capget\0capset\0chdir\0chmod\0chown\0"
	"chown32\0chroot\0clock_adjtime\0clock_getres\0clock_gettime\0clock_nanosleep\0clock_settime\0clone\0clone3\0close\0"
	"close_range\0connect\0copy_file_range\0creat\0create_module\0delete_module\0dup\0dup2\0dup3\0epoll_create\0"
	"epoll_create1\0epoll_ctl\0epoll_pwait\0epoll_pwait2\0epoll_wait\0eventfd\0eventfd2\0execve\0execveat\0exit\0"
	"exit_group\0faccessat\0faccessat2\0fadvise64\0fadvise64_64\0fallocate\0fanotify_init\0fanotify_mark\0fchdir\0fchmod\0"
	"fchmodat\0fchown\0fchown32\0fchownat\0fcntl\0fcntl64\0fdatasync\0fgetxattr\0finit_module\0flistxattr\0"
	"flock\0fork\0fremovexattr\0fsconfig\0fsetxattr\0fsmount\0fsopen\0fspick\0fstat\0fstat64\0"
	"fstatat64\0fstatfs\0fstatfs64\0fsync\0ftruncate\0ftruncate64\0futex\0futex_waitv\0futimesat\0get_kernel_syms\0"
	"get_robust_list\0getcpu\0getcwd\0getdents\0getdents64\0getegid\0getegid32\0geteuid\0geteuid32\0getgid\0"
	"getgid32\0getgroups\0getgroups32\0getitimer\0getpeername\0getpgid\0getpgrp\0getpid\0getpmsg\0getppid\0"
	"getpriority\0getrandom\0getresgid\0getresgid32\0getresuid\0getresuid32\0getrlimit\0getrusage\0getsid\0getsockname\0"
	"getsockopt\0gettid\0gettimeofday\0getuid\0getuid32\0getxattr\0idle\0init_module\0inotify_add_watch\0inotify_init\0"
	"inotify_init1\0inotify_rm_watch\0io_cancel\0io_destroy\0io_getevents\0io_pgetevents\0io_setup\0io_submit\0io_uring_enter\0io_uring_register\0"
	"io_uring_setup\0ioctl\0ioperm\0ioprio_get\0ioprio_set\0ipc\0kcmp\0kexec_file_load\0kexec_load\0keyctl\0"
	"kill\0landlock_add_rule\0landlock_create_ruleset\0landlock_restrict_self\0lchown\0lchown32\0lgetxattr\0link\0linkat\0listen\0"
	"listxattr\0llistxattr\0lremovexattr\0lseek\0lsetxattr\0lstat\0lstat64\0madvise\0membarrier\0memfd_create\0"
	"mincore\0mkdir\0mkdirat\0mknod\0mknodat\0mlock\0mlock2\0mlockall\0mmap\0mmap2\0"
	"mount\0mount_setattr\0move_mount\0mprotect\0mq_getsetattr\0mq_notify\0mq_open\0mq_timedreceive\0mq_timedsend\0mq_unlink\0"
	"mremap\0msync\0munlock\0munlockall\0munmap\0name_to_handle_at\0nanosleep\0nfsservctl\0nice\0open\0"
	"open_by_handle_at\0open_tree\0openat\0openat2\0pause\0perf_event_open\0personality\0pidfd_getfd\0pidfd_open\0pidfd_send_signal\0"
	"pipe\0pipe2\0pivot_root\0pkey_alloc\0pkey_free\0pkey_mprotect\0poll\0ppoll\0prctl\0pread\0"
	"preadv\0preadv2\0prlimit64\0process_madvise\0process_mrelease\0process_vm_readv\0process_vm_writev\0pselect6\0ptrace\0putpmsg\0"
	"pwrite\0pwritev\0pwritev2\0query_module\0quotactl\0quotactl_fd\0read\0readahead\0readdir\0readlink\0"
	"readlinkat\0readv\0reboot\0recvfrom\0recvmmsg\0recvmsg\0remap_file_pages\0removexattr\0rename\0renameat\0"
	"renameat2\0request_key\0rmdir\0rseq\0rt_sigaction\0rt_sigpending\0rt_sigprocmask\0rt_sigqueueinfo\0rt_sigreturn\0rt_sigsuspend\0"
	"rt_sigtimedwait\0rt_tgsigqueueinfo\0s390_pci_mmio_read\0s390_pci_mmio_write\0s390_runtime_instr\0s390_sthyi\0sched_get_priority_max\0sched_get_priority_min\0sched_getaffinity\0sched_getattr\0"
	"sched_getparam\0sched_getscheduler\0sched_rr_get_interval\0sched_setaffinity\0sched_setattr\0sched_setparam\0sched_setscheduler\0sched_yield\0seccomp\0sendfile\0"
	"sendfile64\0sendmmsg\0sendmsg\0sendto\0set_mempolicy_home_node\0set_robust_list\0set_tid_address\0setdomainname\0setfsgid\0setfsgid32\0"
	"setfsuid\0setfsuid32\0setgid\0setgid32\0setgroups\0setgroups32\0sethostname\0setitimer\0setns\0setpgid\0"
	"setpriority\0setregid\0setregid32\0setresgid\0setresgid32\0setresuid\0setresuid32\0setreuid\0setreuid32\0setrlimit\0"
	"setsid\0setsockopt\0settimeofday\0setuid\0setuid32\0setxattr\0shutdown\0sigaction\0sigaltstack\0signal\0"
	"signalfd\0signalfd4\0sigpending\0sigprocmask\0sigreturn\0sigsuspend\0socket\0socketcall\0socketpair\0splice\0"
	"stat\0stat64\0statfs\0statfs64\0statx\0stime\0swapoff\0swapon\0symlink\0symlinkat\0"
	"sync\0sync_file_range\0syncfs\0sysfs\0sysinfo\0syslog\0tee\0tgkill\0time\0timer_create\0"
	"timer_delete\0timer_getoverrun\0timer_gettime\0timer_settime\0timerfd\0timerfd_create\0timerfd_gettime\0timerfd_settime\0times\0tkill\0"
	"truncate\0truncate64\0ugetrlimit\0umask\0umount\0umount2\0uname\0unlink\0unlinkat\0unshare\0"
	"uselib\0userfaultfd\0ustat\0utime\0utimensat\0utimes\0vfork\0vhangup\0vmsplice\0wait4\0"
	"waitid\0write\0writev";
static const unsigned s390_syscall_s2i_s[] = {
	0,8,19,27,35,42,47,55,64,76,
	82,90,95,99,103,113,120,127,133,139,
	145,153,160,174,187,201,217,231,237,244,
	250,262,270,286,292,306,320,324,329,334,
	347,361,371,383,396,407,415,424,431,440,
	445,456,466,477,487,500,510,524,538,545,
	552,561,568,577,586,592,600,610,620,633,
	644,650,655,668,677,687,695,702,709,715,
	723,733,741,751,757,767,779,785,797,807,
	823,839,846,853,862,873,881,891,899,909,
	916,925,935,947,957,969,977,985,992,1000,
	1008,1020,1030,1040,1052,1062,1074,1084,1094,1101,
	1113,1124,1131,1144,1151,1160,1169,1174,1186,1204,
	1217,1231,1248,1258,1269,1282,1296,1305,1315,1330,
	1348,1363,1369,1376,1387,1398,1402,1407,1423,1434,
	1441,1446,1464,1488,1511,1518,1527,1537,1542,1549,
	1556,1566,1577,1590,1596,1606,1612,1620,1628,1639,
	1652,1660,1666,1674,1680,1688,1694,1701,1710,1715,
	1721,1727,1741,1752,1761,1775,1785,1793,1809,1822,
	1832,1839,1845,1853,1864,1871,1889,1899,1910,1915,
	1920,1938,1948,1955,1963,1969,1985,1997,2009,2020,
	2038,2043,2049,2060,2071,2081,2095,2100,2106,2112,
	2118,2125,2133,2143,2159,2176,2193,2211,2220,2227,
	2235,2242,2250,2259,2272,2281,2293,2298,2308,2316,
	2325,2336,2342,2349,2358,2367,2375,2392,2404,2411,
	2420,2430,2442,2448,2453,2466,2480,2495,2511,2524,
	2538,2554,2572,2591,2611,2630,2641,2664,2687,2705,
	2719,2734,2753,2775,2793,2807,2822,2841,2853,2861,
	2870,2881,2890,2898,2905,2929,2945,2961,2975,2984,
	2995,3004,3015,3022,3031,3041,3053,3065,3075,3081,
	3089,3101,3110,3121,3131,3143,3153,3165,3174,3185,
	3195,3202,3213,3226,3233,3242,3251,3260,3270,3282,
	3289,3298,3308,3319,3331,3341,3352,3359,3370,3381,
	3388,3393,3400,3407,3416,3422,3428,3436,3443,3451,
	3461,3466,3482,3489,3495,3503,3510,3514,3521,3526,
	3539,3552,3569,3583,3597,3605,3620,3636,3652,3658,
	3664,3673,3684,3695,3701,3708,3716,3722,3729,3738,
	3746,3753,3765,3771,3777,3787,3794,3800,3808,3817,
	3823,3830,3836,
};
static const int s390_syscall_s2i_i[] = {
	140,142,149,364,33,51,278,124,137,27,
	134,361,351,45,451,184,185,12,15,182,
	212,61,337,261,260,262,259,120,435,6,
	436,362,375,8,127,129,41,63,326,249,
	327,250,312,441,251,318,323,11,354,1,
	248,300,439,253,264,314,332,333,133,94,
	299,95,207,291,55,221,148,229,344,232,
	143,2,235,431,226,432,430,433,108,197,
	293,100,266,118,93,194,238,449,292,130,
	305,311,183,141,220,50,202,49,201,47,
	200,80,205,105,368,132,65,20,188,64,
	96,349,171,211,165,209,76,77,147,367,
	365,236,78,24,199,227,112,128,285,284,
	324,286,247,244,245,382,243,246,426,427,
	425,54,101,283,282,117,343,381,277,280,
	37,445,444,446,16,198,228,9,296,363,
	230,231,234,19,225,107,196,219,356,350,
	218,39,289,14,290,150,374,152,90,192,
	21,442,429,125,276,275,271,274,273,272,
	163,144,151,153,91,335,162,169,34,5,
	336,428,288,437,29,331,136,438,434,424,
	42,325,217,385,386,384,168,302,172,180,
	328,376,334,440,448,340,341,301,26,189,
	181,329,377,167,131,443,3,222,89,85,
	298,145,88,371,357,372,267,233,38,295,
	347,279,40,383,174,176,175,178,173,179,
	177,330,353,352,342,380,159,160,240,346,
	155,157,161,239,345,154,156,158,348,187,
	223,358,370,369,450,304,252,121,139,216,
	138,215,46,214,81,206,74,104,339,57,
	97,71,204,170,210,164,208,70,203,75,
	66,366,79,23,213,224,373,67,186,48,
	316,322,73,126,119,72,359,102,360,306,
	106,195,99,265,379,25,115,87,83,297,
	36,307,338,135,116,103,308,241,13,254,
	258,257,256,255,317,319,321,320,43,237,
	92,193,191,60,22,52,122,10,294,303,
	86,355,62,30,315,313,190,111,309,114,
	281,4,146,
};
static int s390_syscall_s2i(const char *s, int *value) {
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
	return s2i__(s390_syscall_strings, s390_syscall_s2i_s, s390_syscall_s2i_i, 383, copy, value);
	}
}
static const unsigned s390_syscall_i2s_direct[] = {
	440,650,2293,3830,1915,244,-1u,286,1537,3722,
	424,127,3521,1674,133,1511,-1u,-1u,1590,985,
	1721,3701,3226,1144,3422,2220,76,-1u,1963,3771,
	-1u,-1u,35,1910,-1u,3461,1441,2404,1660,2442,
	320,2038,3652,-1u,99,3015,909,3282,891,873,
	42,3708,-1u,1363,586,-1u,3081,-1u,-1u,3695,
	153,3765,324,1000,977,3195,3260,-1u,-1u,3165,
	3101,3341,3308,3053,3185,1074,1084,1131,3213,925,
	3031,-1u,3443,-1u,2316,3746,3436,2342,2308,1710,
	1864,3664,757,545,561,1008,3089,-1u,3400,733,
	1369,3359,3503,3065,947,3388,1606,709,-1u,-1u,
	3800,1169,-1u,3817,3428,3495,1398,751,3331,231,
	2961,3716,-1u,55,1752,3319,292,1174,306,807,
	2272,969,538,82,3489,1985,64,2995,2975,0,
	853,8,644,1839,2336,3836,1094,600,19,1688,
	1845,1701,1853,2807,2719,2822,2734,2841,2641,2664,
	2753,1889,1832,3143,1052,-1u,2259,2095,1899,3121,
	1030,2106,2511,2453,2480,2466,2538,2495,2524,2112,
	2235,139,846,113,120,3270,2861,992,2227,3794,
	3684,1715,3673,767,3393,1612,715,1518,1151,916,
	899,881,3174,3110,935,3041,568,3153,1062,3131,
	1040,145,3233,3022,3004,2984,2049,1652,1620,862,
	592,2298,2870,3242,1596,677,1160,1527,610,1556,
	1566,633,2392,1577,655,1124,3658,779,2775,2687,
	3514,-1u,1296,1258,1269,1305,1248,445,334,361,
	396,2945,477,3526,3583,3569,3552,3539,217,187,
	174,201,-1u,487,3407,741,2375,-1u,-1u,-1u,
	1785,1822,1809,1793,1775,1761,1423,47,2430,1434,
	3823,1387,1376,1204,1186,1231,-1u,1948,1666,1680,
	577,797,723,3729,2411,1542,3451,2325,552,456,
	2211,2100,3738,2929,823,3381,3466,3510,3808,-1u,
	839,371,3787,500,3777,3289,3597,407,3605,3636,
	3620,3298,415,1217,2043,329,347,2118,2242,2554,
	1969,510,524,2133,1871,1920,160,3482,3075,2176,
	2193,2611,1402,620,2793,2705,2420,2853,1020,1639,
	95,2591,2572,431,3753,1628,2358,2881,3352,3370,
	90,262,1549,27,1113,3202,1101,957,2898,2890,
	2349,2367,3251,1694,270,2125,2250,-1u,3416,2630,
	1407,1282,2448,2081,2060,2071,-1u,-1u,-1u,-1u,
	-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,
	-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,
	-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,-1u,
	-1u,-1u,-1u,2020,1348,1315,1330,1938,1741,695,
	668,687,702,2009,237,250,1955,1997,466,2143,
	383,1727,2281,1464,1446,1488,-1u,2159,785,2905,
	103,
};
static const char *s390_syscall_i2s(int v) {
	return i2s_direct__(s390_syscall_strings, s390_syscall_i2s_direct, 1, 451, v);
}
