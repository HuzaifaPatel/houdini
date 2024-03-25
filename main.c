#include "client.h"
#include "vm.h"

int main(){
	unsigned int choice = 1;
	while(choice != 0 && choice < NUM_CHOICES){
		printf("Press 1 to build kernel: ");
		scanf("%d", &choice);
		while (getchar() != '\n');
		make_kernel();
	}
	// if(!connect_to_vm()){
		// send_message("THIS IS A TEST\n");
	// }
	// get_ip_address();
	add_file_to_vm();
	
}