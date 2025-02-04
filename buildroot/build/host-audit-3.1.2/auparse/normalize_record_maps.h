/* This is a generated file, see Makefile.am for its inputs. */
static const char normalize_record_map_strings[] = "aborted-auditd-startup\0access-error\0access-result\0accessed-mac-policy-controlled-object\0accessed-mac-policy-controlled-object\0accessed-policy-controlled-file\0acquired-credentials\0added-group-account-to\0added-mac-network-domain-mapping-to\0added-user-account\0"
	"assigned-user-role-to\0assigned-vm-id\0assigned-vm-resource\0attempted-execution-of-forbidden-program\0attempted-log-in-during-unusual-hour-to\0attempted-log-in-from-unusual-place-to\0audit-error\0authenticated\0authenticated-to-group\0booted-system\0"
	"called-seccomp-controlled-syscall\0caused-account-error\0changed-audit-configuration\0changed-audit-feature\0changed-auditd-configuration\0changed-configuration\0changed-group\0changed-group-password\0changed-login-id-to\0changed-mac-configuration\0"
	"changed-password\0changed-role-to\0changed-selinux-boolean\0changed-selinux-enforcement-to\0changed-selinux-enforcement-to\0changed-socket-promiscuous-mode\0changed-to-runlevel\0changed-user-id\0checked-integrity-of\0configured-device\0"
	"crashed-program\0created-suspicious-file\0created-vm-image\0crypto-officer-logged-in\0crypto-officer-logged-out\0deleted-group-account-from\0deleted-mac-network-domain-mapping-from\0deleted-user-account\0deleted-vm-image\0disposed-credentials\0"
	"ended-session\0failed-log-in-too-many-times-to\0initialized-audit-subsystem\0installed-software\0io_uring-operation\0issued-vm-control\0loaded-kernel-module\0loaded-mac-policy\0loaded-selinux-policy\0locked-account\0"
	"logged-in\0logged-out\0mac-permission\0migrated-vm-from\0migrated-vm-to\0modified-group-account\0modified-level-of\0modified-role\0modified-user-account\0negotiated-crypto-key\0"
	"opened-too-many-sessions-to\0overrode-label-of\0ran-command\0reconfigured-auditd\0refreshed-credentials\0relabeled-filesystem\0remote-audit-connected\0remote-audit-disconnected\0removed-use-role-from\0resumed-audit-logging\0"
	"rotated-audit-logs\0sent-message\0sent-test\0shutdown-audit\0shutdown-system\0started-audit\0started-crypto-session\0started-service\0started-session\0stopped-service\0"
	"tested-file-system-integrity-of\0typed\0typed\0unknown\0unlocked-account\0used-suspcious-link\0was-authorized";
static const int normalize_record_map_i2s_i[] = {
	1005,1006,1100,1101,1102,1103,1104,1105,1106,1107,
	1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,
	1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,
	1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,
	1138,1200,1201,1202,1203,1204,1205,1206,1207,1208,
	1209,1305,1319,1326,1328,1330,1331,1336,1400,1403,
	1404,1405,1409,1410,1700,1701,1702,1703,2000,2100,
	2101,2102,2104,2109,2112,2300,2301,2302,2303,2304,
	2309,2310,2311,2312,2313,2402,2403,2404,2407,2500,
	2501,2502,2503,2504,2505,2506,2507,
};
static const unsigned normalize_record_map_i2s_s[] = {
	1803,691,447,2031,1526,158,1176,1910,1197,50,
	737,532,1648,632,1403,1413,238,1138,179,1071,
	36,654,1816,1986,23,1616,1974,908,461,484,
	1841,888,1894,1926,1471,668,1424,1388,1994,945,
	1271,1857,1826,0,603,1628,1784,1762,1691,1714,
	435,553,1980,498,581,1327,126,1290,88,1366,
	794,770,202,1098,856,963,2011,979,1243,1211,
	356,1570,396,1942,315,754,257,1740,1598,1494,
	1670,1348,1512,711,825,1020,1045,1548,1871,1309,
	294,279,924,1003,1159,1439,1456,
};
static const char *normalize_record_map_i2s(int v) {
	return i2s_bsearch__(normalize_record_map_strings, normalize_record_map_i2s_i, normalize_record_map_i2s_s, 97, v);
}
