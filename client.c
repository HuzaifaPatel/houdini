#include "client.h"
int sock = 0, valread;
struct sockaddr_in serv_addr;
char buffer[1024] = {0};

short int connect_to_vm(){
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    // Convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, SERVER_IP, &serv_addr.sin_addr) <= 0) {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }
    return 0;
}

unsigned long send_message(const char* message){
    // Example: sending data
    unsigned long ret = send(sock, message, strlen(message), 0);
    valread = read(sock, buffer, 1024);
    return ret;
}