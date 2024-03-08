#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <unistd.h>
#include <sys/stat.h>
#include <libvirt/libvirt.h>
#include <libvirt/libvirt.h>
#include <guestfs.h>
#define MOUNT_POINT "dirm"
#define FILESYSTEM "/dev/sda"
int get_ip_address();
short int add_file_to_vm();