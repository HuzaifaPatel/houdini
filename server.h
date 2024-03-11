#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 1236 // Use the port number you want the server to listen on
#define MAX_PENDING_CONNECTIONS 10
#define MAX_BUFFER_SIZE 1024