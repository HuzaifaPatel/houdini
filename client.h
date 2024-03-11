#include <stdio.h>
// vsock works with kvm, vmware, hyper-v
#include <sys/socket.h>
#include <linux/vm_sockets.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define PORT 1236
#define SERVER_IP "192.168.122.64"
short int connect_to_vm();
unsigned long send_message(const char* message);