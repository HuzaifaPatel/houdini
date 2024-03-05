#include <stdio.h>
// vsock works with kvm, vmware, hyper-v
#include <sys/socket.h>
#include <linux/vm_sockets.h>

int main(){
	printk("Hello\n");
}