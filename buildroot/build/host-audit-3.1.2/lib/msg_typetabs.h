/* This is a generated file, see Makefile.am for its inputs. */
static const char msg_type_strings[] = "ACCT_LOCK\0ACCT_UNLOCK\0ADD_GROUP\0ADD_USER\0ANOM_ABEND\0ANOM_ACCESS_FS\0ANOM_ADD_ACCT\0ANOM_AMTU_FAIL\0ANOM_CREAT\0ANOM_CRYPTO_FAIL\0"
	"ANOM_DEL_ACCT\0ANOM_EXEC\0ANOM_LINK\0ANOM_LOGIN_ACCT\0ANOM_LOGIN_FAILURES\0ANOM_LOGIN_LOCATION\0ANOM_LOGIN_ROOT\0ANOM_LOGIN_SERVICE\0ANOM_LOGIN_SESSIONS\0ANOM_LOGIN_TIME\0"
	"ANOM_MAX_DAC\0ANOM_MAX_MAC\0ANOM_MK_EXEC\0ANOM_MOD_ACCT\0ANOM_ORIGIN_FAILURES\0ANOM_PROMISCUOUS\0ANOM_RBAC_FAIL\0ANOM_RBAC_INTEGRITY_FAIL\0ANOM_ROOT_TRANS\0ANOM_SESSION\0"
	"AVC\0AVC_PATH\0BPF\0BPRM_FCAPS\0CAPSET\0CHGRP_ID\0CHUSER_ID\0CONFIG_CHANGE\0CRED_ACQ\0CRED_DISP\0"
	"CRED_REFR\0CRYPTO_FAILURE_USER\0CRYPTO_IKE_SA\0CRYPTO_IPSEC_SA\0CRYPTO_KEY_USER\0CRYPTO_LOGIN\0CRYPTO_LOGOUT\0CRYPTO_PARAM_CHANGE_USER\0CRYPTO_REPLAY_USER\0CRYPTO_SESSION\0"
	"CRYPTO_TEST_USER\0CWD\0DAC_CHECK\0DAEMON_ABORT\0DAEMON_ACCEPT\0DAEMON_CLOSE\0DAEMON_CONFIG\0DAEMON_END\0DAEMON_ERR\0DAEMON_RESUME\0"
	"DAEMON_ROTATE\0DAEMON_START\0DEL_GROUP\0DEL_USER\0DEV_ALLOC\0DEV_DEALLOC\0DM_CTRL\0DM_EVENT\0EOE\0EVENT_LISTENER\0"
	"EXECVE\0FANOTIFY\0FD_PAIR\0FEATURE_CHANGE\0FS_RELABEL\0GRP_AUTH\0GRP_CHAUTHTOK\0GRP_MGMT\0INTEGRITY_DATA\0INTEGRITY_EVM_XATTR\0"
	"INTEGRITY_HASH\0INTEGRITY_METADATA\0INTEGRITY_PCR\0INTEGRITY_POLICY_RULE\0INTEGRITY_RULE\0INTEGRITY_STATUS\0IPC\0IPC_SET_PERM\0KERNEL\0KERNEL_OTHER\0"
	"KERN_MODULE\0LABEL_LEVEL_CHANGE\0LABEL_OVERRIDE\0LOGIN\0MAC_CALIPSO_ADD\0MAC_CALIPSO_DEL\0MAC_CHECK\0MAC_CIPSOV4_ADD\0MAC_CIPSOV4_DEL\0MAC_CONFIG_CHANGE\0"
	"MAC_IPSEC_ADDSA\0MAC_IPSEC_ADDSPD\0MAC_IPSEC_DELSA\0MAC_IPSEC_DELSPD\0MAC_IPSEC_EVENT\0MAC_MAP_ADD\0MAC_MAP_DEL\0MAC_POLICY_LOAD\0MAC_STATUS\0MAC_UNLBL_ALLOW\0"
	"MAC_UNLBL_STCADD\0MAC_UNLBL_STCDEL\0MMAP\0MQ_GETSETATTR\0MQ_NOTIFY\0MQ_OPEN\0MQ_SENDRECV\0NETFILTER_CFG\0NETFILTER_PKT\0OBJ_PID\0"
	"OPENAT2\0PATH\0PROCTITLE\0RESP_ACCT_LOCK\0RESP_ACCT_LOCK_TIMED\0RESP_ACCT_REMOTE\0RESP_ACCT_UNLOCK_TIMED\0RESP_ALERT\0RESP_ANOMALY\0RESP_EXEC\0"
	"RESP_HALT\0RESP_KILL_PROC\0RESP_ORIGIN_BLOCK\0RESP_ORIGIN_BLOCK_TIMED\0RESP_ORIGIN_UNBLOCK_TIMED\0RESP_SEBOOL\0RESP_SINGLE\0RESP_TERM_ACCESS\0RESP_TERM_LOCK\0ROLE_ASSIGN\0"
	"ROLE_MODIFY\0ROLE_REMOVE\0SECCOMP\0SELINUX_ERR\0SERVICE_START\0SERVICE_STOP\0SOCKADDR\0SOCKETCALL\0SOFTWARE_UPDATE\0SYSCALL\0"
	"SYSTEM_BOOT\0SYSTEM_RUNLEVEL\0SYSTEM_SHUTDOWN\0TEST\0TIME_ADJNTPVAL\0TIME_INJOFFSET\0TRUSTED_APP\0TTY\0URINGOP\0USER\0"
	"USER_ACCT\0USER_AUTH\0USER_AVC\0USER_CHAUTHTOK\0USER_CMD\0USER_DEVICE\0USER_END\0USER_ERR\0USER_LABELED_EXPORT\0USER_LOGIN\0"
	"USER_LOGOUT\0USER_MAC_CONFIG_CHANGE\0USER_MAC_POLICY_LOAD\0USER_MAC_STATUS\0USER_MGMT\0USER_ROLE_CHANGE\0USER_SELINUX_ERR\0USER_START\0USER_TTY\0USER_UNLABELED_EXPORT\0"
	"USYS_CONFIG\0VIRT_CONTROL\0VIRT_CREATE\0VIRT_DESTROY\0VIRT_INTEGRITY_CHECK\0VIRT_MACHINE_ID\0VIRT_MIGRATE_IN\0VIRT_MIGRATE_OUT\0VIRT_RESOURCE";
static const unsigned msg_type_s2i_s[] = {
	0,10,22,32,41,52,67,81,96,107,
	124,138,148,158,174,194,214,230,249,269,
	285,298,311,324,338,359,376,391,416,432,
	445,449,458,462,473,480,489,499,513,522,
	532,542,562,576,592,608,621,635,660,679,
	694,711,715,725,738,752,765,779,790,801,
	815,829,842,852,861,871,883,891,900,904,
	919,926,935,943,958,969,978,992,1001,1016,
	1036,1051,1070,1084,1106,1121,1138,1142,1155,1162,
	1175,1187,1206,1221,1227,1243,1259,1269,1285,1301,
	1319,1335,1352,1368,1385,1401,1413,1425,1441,1452,
	1468,1485,1502,1507,1521,1531,1539,1551,1565,1579,
	1587,1595,1600,1610,1625,1646,1663,1686,1697,1710,
	1720,1730,1745,1763,1787,1813,1825,1837,1854,1869,
	1881,1893,1905,1913,1925,1939,1952,1961,1972,1988,
	1996,2008,2024,2040,2045,2060,2075,2087,2091,2099,
	2104,2114,2124,2133,2148,2157,2169,2178,2187,2207,
	2218,2230,2253,2274,2290,2300,2317,2334,2345,2354,
	2376,2388,2401,2413,2426,2447,2463,2479,2496,
};
static const int msg_type_s2i_i[] = {
	1135,1136,1116,1114,1701,2111,2114,2107,1703,2110,
	2115,2112,1702,2103,2100,2104,2119,2118,2102,2101,
	2105,2106,2113,2116,2120,1700,2108,2109,2117,2121,
	1400,1402,1334,1321,1322,1119,1125,1305,1103,1104,
	1110,2405,2408,2409,2404,2402,2403,2401,2406,2407,
	2400,1307,1118,1202,1207,1208,1203,1201,1209,1206,
	1205,1200,1117,1115,2307,2308,1338,1339,1320,1335,
	1309,1331,1317,1328,2309,1126,1133,1132,1800,1806,
	1803,1801,1804,1807,1805,1802,1303,1311,2000,1316,
	1330,2304,2303,1006,1418,1419,1134,1407,1408,1405,
	1411,1413,1412,1414,1415,1409,1410,1403,1404,1406,
	1416,1417,1323,1315,1314,1312,1313,1325,1324,1318,
	1337,1302,1327,2207,2205,2204,2206,2201,2200,2210,
	2212,2202,2213,2214,2215,2209,2211,2203,2208,2301,
	2311,2302,1326,1401,1130,1131,1306,1304,1138,1300,
	1127,1129,1128,1120,1333,1332,1121,1319,1336,1005,
	1101,1100,1107,1108,1123,1137,1106,1109,2305,1112,
	1113,2312,2310,2313,1102,2300,1122,1105,1124,2306,
	1111,2500,2504,2505,2503,2502,2506,2507,2501,
};
static int msg_type_s2i(const char *s, int *value) {
	size_t len, i;
	 if (s == NULL || value == NULL)
		return 0;
	len = strlen(s);
	{ char copy[len + 1];
	for (i = 0; i < len; i++) {
		char c = s[i];
		copy[i] = GT_ISLOWER(c) ? c - 'a' + 'A' : c;
	}
	copy[i] = 0;
	return s2i__(msg_type_strings, msg_type_s2i_s, msg_type_s2i_i, 189, copy, value);
	}
}
static const int msg_type_i2s_i[] = {
	1005,1006,1100,1101,1102,1103,1104,1105,1106,1107,
	1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,
	1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,
	1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,
	1138,1200,1201,1202,1203,1205,1206,1207,1208,1209,
	1300,1302,1303,1304,1305,1306,1307,1309,1311,1312,
	1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,
	1323,1324,1325,1326,1327,1328,1330,1331,1332,1333,
	1334,1335,1336,1337,1338,1339,1400,1401,1402,1403,
	1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,
	1414,1415,1416,1417,1418,1419,1700,1701,1702,1703,
	1800,1801,1802,1803,1804,1805,1806,1807,2000,2100,
	2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,
	2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,
	2121,2200,2201,2202,2203,2204,2205,2206,2207,2208,
	2209,2210,2211,2212,2213,2214,2215,2300,2301,2302,
	2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,
	2313,2400,2401,2402,2403,2404,2405,2406,2407,2408,
	2409,2500,2501,2502,2503,2504,2505,2506,2507,
};
static const unsigned msg_type_i2s_s[] = {
	2099,1221,2114,2104,2290,513,522,2334,2169,2124,
	2133,2178,532,2376,2207,2218,32,852,22,842,
	715,480,2040,2075,2317,2148,2345,489,969,1996,
	2024,2008,1925,1939,992,978,1259,0,10,2157,
	1972,829,779,725,765,815,801,738,752,790,
	1988,1595,1138,1961,499,1952,711,919,1142,1531,
	1539,1521,1507,1162,935,1579,2087,900,462,473,
	1502,1565,1551,1905,1600,943,1175,926,2060,2045,
	458,904,2091,1587,883,891,445,1913,449,1425,
	1441,1301,1452,1269,1285,1401,1413,1319,1352,1335,
	1368,1385,1468,1485,1227,1243,359,41,148,96,
	1001,1051,1121,1036,1070,1106,1016,1084,1155,174,
	269,249,158,194,285,298,81,376,391,107,
	52,138,311,67,124,324,416,230,214,338,
	432,1697,1686,1730,1837,1646,1625,1663,1610,1854,
	1813,1710,1825,1720,1745,1763,1787,2300,1869,1893,
	1206,1187,2187,2354,861,871,958,2253,1881,2230,
	2274,694,635,608,621,592,542,660,679,562,
	576,2388,2496,2447,2426,2401,2413,2463,2479,
};
static const char *msg_type_i2s(int v) {
	return i2s_bsearch__(msg_type_strings, msg_type_i2s_i, msg_type_i2s_s, 189, v);
}
