#include "client.h"
#include "view.h"
#include <termios.h>
#include <unistd.h>
#include <sys/wait.h>

int file_str(char* str){
    // Step 1: Open the file
    file = fopen("output.txt", "a");
    fprintf(file, "%s\n", str);
    // Step 2: Check for errors
/*    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }*/
    fflush(file);
    fclose(file);
}

int file_int(int num){
    // Step 1: Open the file
    file = fopen("output.txt", "a");
    fprintf(file, "%d\n", num);
    // Step 2: Check for errors
/*    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }*/
    fflush(file);
    fclose(file);
}

void printStringInHex(const char *str) {
    while (*str) {
        printf("%02x ", (unsigned char) *str);
        str++;
    }
    printf("\n");
}

const char* user_opts[] = {
    "1: Build Kernel",
    "2: View Docker Version",
    "3: Set Kernel Version",
    "4: View Set Kernel Version",
    "5: Set Docker Version",
    "6: Start Virtual Machine",
    "7: Exit",
    NULL
};

int (*func_lut[])() = {
    make_kernel, //1
    list_docker_versions, //2
    set_kernel_version, //3
    view_set_kernel_version, //4
    set_docker_version, //5
    start_virtual_machine, //6
    exit_houdini,//7
    NULL //8
};

const char* dock_v[] = {
    "17.03.0-ce",
    "17.03.1-ce",
    "17.03.2-ce",
    "17.06.0-ce",
    "17.06.1-ce",
    "17.06.2-ce",
    "17.09.0-ce",
    "17.09.1-ce",
    "17.12.0-ce",
    "17.12.1-ce",
    "18.03.0-ce",
    "18.03.1-ce",
    "18.06.0-ce",
    "18.06.1-ce",
    "18.06.2-ce",
    "18.06.3-ce",
    "18.09.0",
    "18.09.1",
    "18.09.2",
    "18.09.3",
    "18.09.4",
    "18.09.5",
    "18.09.6",
    "18.09.7",
    "18.09.8",
    "18.09.9",
    "19.03.0",
    "19.03.1",
    "19.03.10",
    "19.03.11",
    "19.03.12",
    "19.03.13",
    "19.03.14",
    "19.03.15",
    "19.03.2",
    "19.03.3",
    "19.03.4",
    "19.03.5",
    "19.03.6",
    "19.03.7",
    "19.03.8",
    "19.03.9",
    "20.10.0",
    "20.10.1",
    "20.10.10",
    "20.10.11",
    "20.10.12",
    "20.10.13",
    "20.10.14",
    "20.10.15",
    "20.10.16",
    "20.10.17",
    "20.10.18",
    "20.10.19",
    "20.10.2",
    "20.10.20",
    "20.10.21",
    "20.10.22",
    "20.10.23",
    "20.10.24",
    "20.10.3",
    "20.10.4",
    "20.10.5",
    "20.10.6",
    "20.10.7",
    "20.10.8",
    "20.10.9",
    "23.0.0",
    "23.0.1",
    "23.0.2",
    "23.0.3",
    "23.0.4",
    "23.0.5",
    "23.0.6",
    "24.0.0",
    "24.0.1",
    "24.0.2",
    "24.0.3",
    "24.0.4",
    "24.0.5",
    "24.0.6",
    "24.0.7",
    "24.0.8",
    "24.0.9",
    "25.0.0",
    "25.0.1",
    "25.0.2",
    "25.0.3",
    "25.0.4",
    "25.0.5",
    "26.0.0",
    NULL
};

void init(){
    fetch_kernel_versions();
}

int exit_houdini(){
    for(int i = 0; i < num_kernel_version; i++){
        free(kernel_versions[i]);
    }

    if(num_kernel_version){
        free(kernel_versions);
        num_kernel_version = 0;
    }

    for(int i = 0; i < num_cached_kernels; i++){
        free(cached_kernel_versions[i]);
    }

    if(num_cached_kernels){
        free(cached_kernel_versions);
        num_cached_kernels = 0;
    }

    exit(0);
}

const int num_user_opts = sizeof(user_opts) / sizeof(user_opts[0]);
// const int dock_v = sizeof(dock_v) / sizeof(dock_v[0]);
int sock = 0, valread;
struct sockaddr_in serv_addr;
char buffer[1024] = {0};


// Function to get a character from stdin without needing to press enter
int getch(void) {
    struct termios oldattr, newattr;
    int ch;
    tcgetattr(STDIN_FILENO, &oldattr);
    newattr = oldattr;
    newattr.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newattr);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldattr);
    return ch;
}


void display_main_menu(int selected, int offset) {
    printf("\x1b[H\x1b[J");  // Clear screen
    for (int i = offset; i < NUM_CHOICES; i++) {
        if (i == selected) {
            printf("\x1b[7m%s\x1b[0m\n", user_opts[i]);  // Highlight selected
        } else {
            printf("%s\n", user_opts[i]);  // Normal display
        }
    }
    fflush(stdout);
}


int set_docker_version(){
    return 0;
}


int set_main_menu(){
    int selected = 0;
    int offset = 0;  // offset is not needed without scrolling
    display_main_menu(selected, offset);

    while (1) {
        int ch = getch();
        if (ch == '\033') {
            int l = getch();  // Skip '['
            int switch_case = getch();
            switch (switch_case) {
                case 'A':  // Up arrow
                    if (selected == 0) {
                        selected = NUM_CHOICES - 1; // Loop back to the end
                    } else {
                        selected--;
                    }
                    break;
                case 'B':  // Down arrow
                    if (selected == NUM_CHOICES - 1) {
                        selected = 0; // Loop back to the start
                    } else {
                        selected++;
                    }
                    break;
                default:
                    break;
            }
        } else if (ch == '\n') {
            func_lut[selected]();
            break;  // Exit on Enter key
        }

        display_main_menu(selected, offset);
    }

    printf("Selected option: %s\n", user_opts[selected]);
    return 0;
}


void display_kernel_version_menu(int selected, int offset) {
    printf("\x1b[H\x1b[J");  // Clear screen
    printf("Select Kernel Version by Pressing the Down Arrow. Enter 'n' to Exit\n");
    int display_limit = (num_kernel_version < offset + MAX_DISPLAY_KERNEL) ? num_kernel_version : offset + MAX_DISPLAY_KERNEL;
    for (int i = offset; i < display_limit; i++) {
        if (i == selected) {
            printf("\x1b[7m%s\x1b[0m", kernel_versions[i]);  // Highlight selected
        } else {
            printf("%s\n", kernel_versions[i]);  // Normal display
        }
    }
    fflush(stdout);
}


int set_kernel_version() {
    int selected = 0;
    int offset = 0;  // To handle scrolling

    display_kernel_version_menu(selected, offset);

    while (1) {
        int ch = getch();
        if (ch == '\033') {
            // Check if this is a single ESC key press or part of an arrow key sequence
            int next_char = getch();  // Read the next character to determine the key press
            if (next_char == '[') {  // This is part of an arrow key sequence
                switch (getch()) {  // Read the final character in the sequence
                    case 'A':  // Up arrow
                        if (selected > 0) {
                            selected--;
                            if (selected < offset) {
                                offset--;
                            }
                        }
                        break;
                    case 'B':  // Down arrow
                        if (selected < num_kernel_version - 1) {
                            selected++;
                            if (selected >= offset + MAX_DISPLAY_KERNEL) {
                                offset++;
                            }
                        }
                        break;
                    default:
                        break;
                }
            }
        } else if (ch == '\n') {
            break;  // Exit on Enter key
        } else if(ch == 'n'){
            // This was a single ESC key press
            return 0;  // Return to the previous function/menu
        }
        
        display_kernel_version_menu(selected, offset);
    }

    make_new_config_yml(kernel_versions[selected]);
    write_new_config_yml();
    return 0;
}


int make_kernel(){
    clear_screen();
    int status = system("ansible-playbook make_kernel.yml -i hosts.ini -e @config/config.yml");

    if (status == -1) {
        printf("Failed to execute command\n");
        return 1;
    }

    return 0;
}

int list_docker_versions(){
    int num_versions = sizeof(dock_v) / sizeof(dock_v[0]);

    for (int i = 0; dock_v[i] != NULL; i++) {
        printf("%s\n", dock_v[i]);
    }
    return 0;
}

int fetch_kernel_versions(){
    ssize_t read;
    char* line = NULL;
    size_t len = 0;
    kernel_versions = malloc(sizeof(char *));  // Allocate an array for one string pointer
    

    if (!kernel_versions) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    FILE *fp = popen("python3 parse_kernel_versions.py b", "r");
    if (fp == NULL) {
        fprintf(stderr, "Failed to run Python script\n");
        return 1;
    }

    while ((read = getline(&line, &len, fp)) != -1) {
        kernel_versions[num_kernel_version++] = strdup(line);
        kernel_versions = realloc(kernel_versions, (num_kernel_version + 1) * sizeof(char*));
    }

    pclose(fp);
}

int view_set_kernel_version(){
    ssize_t read;
    char * line = NULL;
    size_t len = 0;
    while(1){
        clear_screen();
        printnnl("Press 'n' to go back.\nThe Following Kernel Version is Set: ");
        FILE *fp = popen("python3 parse_kernel_versions.py c", "r");
        if (fp == NULL) {
            fprintf(stderr, "Failed to run Python script\n");
            return 1;
        }

        while ((read = getline(&line, &len, fp)) != -1) {
            printf("\033[31m%s\033[0m", line);
        }

        pclose(fp);
        
        if(getch() == 'n'){
            return 0;
        }
    }
}

int make_new_config_yml(char* new_kernel_version){
    FILE* file = fopen(CONFIG_FILE, "r");
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    num_config_yml_lines = 0;
    config_yml = malloc(sizeof(char*));
    int size;
    char* command;

    if (file == NULL) {
        fprintf(stderr, "Failed to run %s\n", CONFIG_FILE);
        return 1;
    }

    // rempve \n from new_kernel_version
    size_t len_new_kernel_version = strlen(new_kernel_version);
    if (len_new_kernel_version > 0 && new_kernel_version[len_new_kernel_version - 1] == '\n') {
        new_kernel_version[len_new_kernel_version - 1] = '\0';
    }

    while ((read = getline(&line, &len, file)) != -1) {

        if (strstr(line, "BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE") || strstr(line, "BR2_LINUX_KERNEL_VERSION")) {
            snprintf(line, len, "  - '%s=\"%s\"'\n", strstr(line, "BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE") ? "BR2_LINUX_KERNEL_CUSTOM_VERSION_VALUE" : "BR2_LINUX_KERNEL_VERSION", new_kernel_version);
        }

        config_yml[num_config_yml_lines++] = strdup(line);
        config_yml = realloc(config_yml, (num_config_yml_lines + 1) * sizeof(char*));
    }

    size = snprintf(NULL, 0, "python3 parse_kernel_versions.py d %s", new_kernel_version) + 1;
    command = malloc(sizeof(char) * size);
    snprintf(command, size, "python3 parse_kernel_versions.py d %s", new_kernel_version) + 1;
    system(command);
    fclose(file);
    return 0;
}

int write_new_config_yml(){
    FILE *file = fopen(CONFIG_FILE, "w"); // Open the file for writing, which truncates it if it exists
    
    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }

    for(int i = 0; i < num_config_yml_lines; i++){
        // Write new content to the file
        fprintf(file, "%s", config_yml[i]);
    }

    fclose(file);
    return 0;
}


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

void clear_cache_list(){
    for(int i = 0; i < num_cached_kernels; i++){
        free(cached_kernel_versions[i]);
    }
    if(num_cached_kernels){
        free(cached_kernel_versions);
        num_cached_kernels = 0;
    }
}


int fetch_cached_kernels(){
    DIR *dir;
    struct dirent *entry;
    clear_screen();
    dir = opendir("cache/kernels/");
    num_cached_kernels = 0;    
    
    if (dir == NULL) {
        perror("opendir");
        return 1;
    }

    printf("Press 'n' to go back.\n\nDirectories in cache/kernel/:\n");
    while ((entry = readdir(dir)) != NULL) {
        // Check if the entry is a directory (but not '.' or '..')
        if (entry->d_type == DT_DIR && strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {
            cached_kernel_versions = realloc(cached_kernel_versions, (num_cached_kernels + 1) * sizeof(char *));
            if(cached_kernel_versions == NULL){
                printf("FAILED REALLOC");
                return 1;
            }
            cached_kernel_versions[num_cached_kernels] = strdup(entry->d_name);
            num_cached_kernels++;
        }
    }
    closedir(dir);
}

int display_cached_kernel_versions(int selected, int offset){
    printf("\x1b[H\x1b[J");  // Clear screen
    printf("Select Cached Kernel Version to Start Virtual Machine. Enter 'n' to Exit\n");
    int display_limit = (num_cached_kernels < offset + MAX_DISPLAY_KERNEL) ? num_cached_kernels : offset + MAX_DISPLAY_KERNEL;
    for (int i = offset; i < num_cached_kernels; i++) {
        if (i == selected) {
            printf("\x1b[7m%s\x1b[0m\n", cached_kernel_versions[i]);  // Highlight selected
        } else {
            printf("%s\n", cached_kernel_versions[i]);  // Normal display
        }
    }
    fflush(stdout);
}

int cached_kernel_versions_menu(){
    fetch_cached_kernels(); // put stuff in array
    printf("%d\n", num_cached_kernels);
    int selected = 0;
    int offset = 0;  // To handle scrolling

    display_cached_kernel_versions(selected, offset);

    while (1) {
        int ch = getch();
        if (ch == '\033') {
            // Check if this is a single ESC key press or part of an arrow key sequence
            int next_char = getch();  // Read the next character to determine the key press
            if (next_char == '[') {  // This is part of an arrow key sequence
                switch (getch()) {  // Read the final character in the sequence
                    case 'A':  // Up arrow
                        if (selected > 0) {
                            selected--;
                            if (selected < offset) {
                                offset--;
                            }
                        }
                        break;
                    case 'B':  // Down arrow
                        if (selected < num_cached_kernels - 1) {
                            selected++;
                            if (selected >= offset + MAX_DISPLAY_KERNEL) {
                                offset++;
                            }
                        }
                        break;
                    default:
                        break;
                }
            }
        } else if (ch == '\n') {
            run_kernel = cached_kernel_versions[selected];
            return 0;  // Exit on Enter key
        } else if(ch == 'n'){ // check if 'n' is pressed
            return 0;  // Return to the previous function/menu
        }
        
        display_cached_kernel_versions(selected, offset);
    }
}

int start_virtual_machine(){
    cached_kernel_versions_menu();
    file_str("hel");
    // int size;
    char *kernel_image = malloc(sizeof(char) * (sizeof("cache/kernels/images/bzImage") + sizeof(run_kernel)) + 1);  // Replace with actual path
    char *rootfs_image = malloc(sizeof(char) * (sizeof("file=cache/kernels/images/rootfs.ext2,format=raw,if=virtio") + sizeof(run_kernel)) + 1);  // Replace with actual path
    
    if(kernel_image == NULL || rootfs_image == NULL){
        perror("Malloc Failed");
        return 1;
    }
    
    snprintf(kernel_image, sizeof(char) * (sizeof("cache/kernels/images/bzImage") + sizeof(run_kernel)), "cache/kernels/%s/images/bzImage", run_kernel);
    snprintf(rootfs_image, sizeof(char) * (sizeof("file=cache/kernels/images/rootfs.ext2,format=raw,if=virtio") + sizeof(run_kernel)), "file=cache/kernels/%s/images/rootfs.ext2,format=raw,if=virtio", run_kernel);

    file_str(kernel_image);
    file_str(rootfs_image);

    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        if (execlp("qemu-system-x86_64", "qemu-system-x86_64", "-drive", rootfs_image, "-kernel", kernel_image, "-append", "console=tty0", "-netdev", "user,id=usernet", "-device", "virtio-net,netdev=usernet", (char *)NULL) == -1) {
            file_str("execlp");
            exit(EXIT_FAILURE);
        }
    } else {
        // Parent process
        file_int(pid);        
        int status;
        waitpid(pid, &status, 0);  // Wait for the child process to finish
        
        if (WIFEXITED(status)) {
            printf("Child exited with status %d\n", WEXITSTATUS(status));
        }
    }

    // free(command);
    clear_screen();
    return 0;
}

void clear_screen() {
    printf("\x1b[2J\x1b[H");  // Clear screen and move cursor to home position
    fflush(stdout);  // Ensure the command is sent to the terminal immediately
}