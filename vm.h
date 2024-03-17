#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <unistd.h>
#include <sys/stat.h>
#include <libvirt/libvirt.h>
#include <guestfs.h>
#include <string.h>
#define FILESYSTEM "/dev/sda1"
int get_ip_address();
short int add_file_to_vm();
