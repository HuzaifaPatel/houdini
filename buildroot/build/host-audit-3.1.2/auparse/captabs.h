/* This is a generated file, see Makefile.am for its inputs. */
static const char cap_strings[] = "audit_control\0audit_read\0audit_write\0block_suspend\0bpf\0checkpoint_restore\0chown\0dac_override\0dac_read_search\0fowner\0"
	"fsetid\0ipc_lock\0ipc_owner\0kill\0lease\0linux_immutable\0mac_admin\0mac_override\0mknod\0net_admin\0"
	"net_bind_service\0net_broadcast\0net_raw\0perfmon\0setfcap\0setgid\0setpcap\0setuid\0sys_admin\0sys_boot\0"
	"sys_chroot\0sys_module\0sys_nice\0sys_pacct\0sys_ptrace\0sys_rawio\0sys_resource\0sys_time\0sys_tty_config\0syslog\0"
	"wake_alarm";
static const unsigned cap_i2s_direct[] = {
	74,80,93,109,116,142,263,278,270,153,
	208,225,198,239,123,132,315,356,304,345,
	335,285,295,326,366,379,388,192,147,25,
	0,255,179,169,403,410,37,14,247,51,
	55,
};
static const char *cap_i2s(int v) {
	return i2s_direct__(cap_strings, cap_i2s_direct, 0, 40, v);
}
