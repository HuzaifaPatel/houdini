/* This is a generated file, see Makefile.am for its inputs. */
static const char type_strings[] = "a0\0a1\0a2\0a3\0acct\0action\0addr\0arch\0auid\0cap_fi\0"
	"cap_fp\0cap_pa\0cap_pe\0cap_pi\0cap_pp\0capability\0cgroup\0cmd\0code\0comm\0"
	"cwd\0data\0device\0dir\0egid\0errno\0euid\0exe\0exit\0family\0"
	"fan_info\0fan_type\0fi\0file\0flags\0fp\0fsgid\0fsuid\0gid\0grp\0"
	"hook\0icmptype\0id\0igid\0img-ctx\0inode_gid\0inode_uid\0invalid_context\0ioctlcmd\0iuid\0"
	"key\0list\0macproto\0mode\0name\0new-chardev\0new-disk\0new-fs\0new-net\0new-rng\0"
	"new_gid\0new_group\0new_pe\0new_pi\0new_pp\0nl-mcgrp\0oauid\0obj\0obj_gid\0obj_trust\0"
	"obj_uid\0ocomm\0oflag\0ogid\0old-auid\0old-chardev\0old-disk\0old-fs\0old-net\0old-rng\0"
	"old_pa\0old_pe\0old_pi\0old_pp\0old_prom\0ouid\0pa\0path\0pe\0per\0"
	"perm\0perm_mask\0pi\0pp\0proctitle\0prom\0proto\0res\0resolve\0resp\0"
	"result\0root_dir\0saddr\0sauid\0scontext\0ses\0sgid\0sig\0sigev_signo\0subj\0"
	"subj_trust\0suid\0sw\0syscall\0tcontext\0uid\0uring_op\0vm\0vm-ctx\0watch";
static const unsigned type_s2i_s[] = {
	0,3,6,9,12,17,24,29,34,39,
	46,53,60,67,74,81,92,99,103,108,
	113,117,122,129,133,138,144,149,153,158,
	165,174,183,186,191,197,200,206,212,216,
	220,225,234,237,242,250,260,270,286,295,
	300,304,309,318,323,328,340,349,356,364,
	372,380,390,397,404,411,420,426,430,438,
	448,456,462,468,473,482,494,503,510,518,
	526,533,540,547,554,563,568,571,576,579,
	583,588,598,601,604,614,619,625,629,637,
	642,649,658,664,670,679,683,688,692,704,
	709,720,725,728,736,745,749,758,761,768,
};
static const int type_s2i_i[] = {
	14,15,16,17,6,35,26,4,1,22,
	22,22,22,22,22,12,6,6,28,6,
	6,20,6,6,2,46,1,6,5,23,
	45,44,22,6,30,22,2,1,2,6,
	34,24,1,2,32,2,1,6,37,1,
	38,19,36,8,39,6,6,6,6,6,
	2,6,22,22,22,41,1,32,2,43,
	1,6,29,2,1,6,6,6,6,6,
	22,22,22,22,11,1,22,6,22,27,
	7,7,22,22,33,11,25,13,42,40,
	13,6,9,1,32,21,2,18,18,32,
	43,1,6,3,32,1,3,6,32,6,
};
static int type_s2i(const char *s, int *value) {
	return s2i__(type_strings, type_s2i_s, type_s2i_i, 120, s, value);
}
