#ifndef CLIENT_H
#define CLIENT_H

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
// vsock works with kvm, vmware, hyper-v
#include <sys/socket.h>
#include <linux/vm_sockets.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define PORT 1236
#define SERVER_IP "192.168.122.64"
#define CONFIG_FILE "config/config.yml"
#define NUM_CHOICES 7
#define MAX_DISPLAY_KERNEL 1  // Maximum number of items to display at once
short int connect_to_vm();
unsigned long send_message(const char* message);
int make_kernel();
int fetch_kernel_versions();
int list_docker_versions();
int set_kernel_version();
int set_docker_version();
int make_new_config_yml(char* new_kernel_version);
int write_new_config_yml();
void display_main_menu();
int start_virtual_machine();
int set_main_menu();
void init();
void clear_screen();
int exit_houdini();
int view_set_kernel_version();
int display_cached_kernel_versions(int selected, int offset);
int cached_kernel_versions_menu();
void display_menu(int selected, int offset);
int getch(void);
int fetch_cached_kernels();
void printStringInHex(const char *str);
static char** cached_kernel_versions;
static int num_cached_kernels;
static int num_kernel_version;
static char** kernel_versions;
static char* run_kernel; // user chooses which kernel to run based on cache
extern const char* user_opts[];
extern const char* dock_v[];
extern const int num_user_opts;
static char** config_yml;
static int num_config_yml_lines;
extern int (*func_lut[])();
int file_str(char* str);
int file_int(int num);
static FILE* file;
// extern const int dock_v;


#endif