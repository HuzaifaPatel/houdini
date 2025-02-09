/* This is a generated file, see Makefile.am for its inputs. */
static const char prctl_opt_strings[] = "PR_CAPBSET_DROP\0PR_CAPBSET_READ\0PR_CAP_AMBIENT\0PR_GET_CHILD_SUBREAPER\0PR_GET_DUMPABLE\0PR_GET_ENDIAN\0PR_GET_FPEMU\0PR_GET_FPEXC\0PR_GET_FP_MODE\0PR_GET_IO_FLUSHER\0"
	"PR_GET_KEEPCAPS\0PR_GET_MDWE\0PR_GET_MEMORY_MERGE\0PR_GET_NAME\0PR_GET_NO_NEW_PRIVS\0PR_GET_PDEATHSIG\0PR_GET_SECCOMP\0PR_GET_SECUREBITS\0PR_GET_SPECULATION_CTRL\0PR_GET_TAGGED_ADDR_CTRL\0"
	"PR_GET_THP_DISABLE\0PR_GET_TID_ADDRESS\0PR_GET_TIMERSLACK\0PR_GET_TIMING\0PR_GET_TSC\0PR_GET_UNALIGN\0PR_MCE_KILL\0PR_MCE_KILL_GET\0PR_MPX_DISABLE_MANAGEMENT\0PR_MPX_ENABLE_MANAGEMENT\0"
	"PR_PAC_GET_ENABLED_KEYS\0PR_PAC_RESET_KEYS\0PR_PAC_SET_ENABLED_KEYS\0PR_RISCV_V_GET_CONTROL\0PR_RISCV_V_SET_CONTROL\0PR_SCHED_CORE\0PR_SET_CHILD_SUBREAPER\0PR_SET_DUMPABLE\0PR_SET_ENDIAN\0PR_SET_FPEMU\0"
	"PR_SET_FPEXC\0PR_SET_FP_MODE\0PR_SET_IO_FLUSHER\0PR_SET_KEEPCAPS\0PR_SET_MDWE\0PR_SET_MEMORY_MERGE\0PR_SET_MM\0PR_SET_NAME\0PR_SET_NO_NEW_PRIVS\0PR_SET_PDEATHSIG\0"
	"PR_SET_SECCOMP\0PR_SET_SECUREBITS\0PR_SET_SPECULATION_CTRL\0PR_SET_SYSCALL_USER_DISPATCH\0PR_SET_TAGGED_ADDR_CTRL\0PR_SET_THP_DISABLE\0PR_SET_TIMERSLACK\0PR_SET_TIMING\0PR_SET_TSC\0PR_SET_UNALIGN\0"
	"PR_SME_GET_VL\0PR_SME_SET_VL\0PR_SVE_GET_VL\0PR_SVE_SET_VL\0PR_TASK_PERF_EVENTS_DISABLE\0PR_TASK_PERF_EVENTS_ENABLE";
static const unsigned prctl_opt_i2s_direct[] = {
	840,239,70,661,418,1029,159,750,100,691,
	113,704,393,1004,808,207,-1u,-1u,86,677,
	256,857,16,0,407,1018,271,872,986,375,
	1100,1128,433,445,798,638,47,820,219,356,
	967,337,487,461,717,126,32,-1u,-1u,1086,
	1072,289,890,536,943,313,732,141,914,554,
	512,624,1058,1044,766,175,778,187,601,578,
};
static const char *prctl_opt_i2s(int v) {
	return i2s_direct__(prctl_opt_strings, prctl_opt_i2s_direct, 1, 70, v);
}
