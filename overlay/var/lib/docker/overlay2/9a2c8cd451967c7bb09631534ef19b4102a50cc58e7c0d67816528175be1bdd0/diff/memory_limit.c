#include <stdio.h>
#include <sys/resource.h>
#include <stdlib.h>

int main() {
    struct rlimit rl;

    // Get the current stack size limit
    if (getrlimit(RLIMIT_STACK, &rl) != 0) {
        perror("Error getting current stack size limit");
        return 1;
    }

    printf("Current stack size: %ld bytes\n", rl.rlim_cur);

    // Set the new stack size limit (e.g., 16 MB)
    rl.rlim_cur = 16 * 1024 * 1024;  // 16 MB in bytes

    if (setrlimit(RLIMIT_STACK, &rl) != 0) {
        perror("Error setting new stack size limit");
        return 1;
    }

    // Verify that the new stack size limit was set
    if (getrlimit(RLIMIT_STACK, &rl) != 0) {
        perror("Error getting updated stack size limit");
        return 1;
    }

    printf("Updated stack size: %ld bytes\n", rl.rlim_cur);

    return 0;
}
