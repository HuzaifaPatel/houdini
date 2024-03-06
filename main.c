#include "client.h"

int main(){
	if(!connect_to_vm()){
		send_message("THIS IS A TEST\n");
	}
}