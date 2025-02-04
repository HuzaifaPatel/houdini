/* This is a generated file, see Makefile.am for its inputs. */
static const char evtype_strings[] = "TTY\0anomaly\0anomaly-response\0audit-daemon\0audit-rule\0av-decision\0bpf-program\0configuration\0crypto\0dac-decision\0"
	"group-change\0integrity\0mac\0mac-decision\0system-services\0unknown\0user-account\0user-login\0user-space\0virt";
static const unsigned evtype_i2s_direct[] = {
	167,199,151,77,0,175,188,29,138,4,
	124,12,134,91,210,42,98,111,53,65,
};
static const char *evtype_i2s(int v) {
	return i2s_direct__(evtype_strings, evtype_i2s_direct, 0, 19, v);
}
