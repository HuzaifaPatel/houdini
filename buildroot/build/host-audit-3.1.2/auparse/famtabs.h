/* This is a generated file, see Makefile.am for its inputs. */
static const char fam_strings[] = "alg\0appletalk\0ash\0atmpvc\0atmsvc\0ax25\0bluetooth\0bridge\0caif\0can\0"
	"decnet\0econet\0ieee802154\0inet\0inet6\0ipx\0irda\0isdn\0iucv\0kcm\0"
	"key\0llc\0local\0mctp\0netbeui\0netlink\0netrom\0nfc\0packet\0phonet\0"
	"pppox\0qipcrtr\0rds\0rose\0rxrpc\0security\0smc\0sna\0tipc\0vsock\0"
	"wanpipe\0x25\0xdp";
static const unsigned fam_i2s_direct[] = {
	130,88,32,99,4,157,47,18,247,93,
	200,63,141,211,122,149,168,14,70,25,
	196,224,103,182,239,126,-1u,-1u,59,228,
	37,113,205,108,175,77,54,0,164,233,
	118,188,220,251,136,
};
static const char *fam_i2s(int v) {
	return i2s_direct__(fam_strings, fam_i2s_direct, 1, 45, v);
}
