#include "client.h"
#include "view.h"
#include "vm.h"

int main(){
	init();
	unsigned short choice;

	print("Welcome to Houdini");

	while(1){
		set_main_menu();
		// print("");
		// for(short int i = 0; user_opts[i] != NULL; i++){
		// 	print(user_opts[i]);
		// }

		// printnnl("Choice: ");
		// scanf("%hd", &choice);
		// while (getchar() != '\n');
		
	    // // Check if the choice is valid and call the respective function
	    // if (choice > 0 && choice <= NUM_CHOICES)
	    //     (*func_lut[choice - 1])();
	    // else
	    //     print("\n\x1B[31mInvalid choice\x1B[0m");
	// if(!connect_to_vm()){
		// send_message("THIS IS A TEST\n");
	// }
	// get_ip_address();
	// add_file_to_vm();
	}
}