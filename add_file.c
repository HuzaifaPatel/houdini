#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mount.h>

int main() {
    char *image_path = "lol.qcow2";
    char *mount_point = "dirm";

    // Load the nbd kernel module
    if (system("modprobe nbd max_part=63") != 0) {
        fprintf(stderr, "Error: Failed to load nbd kernel module\n");
        exit(EXIT_FAILURE);
    }

    // Connect the qcow2 image to a network block device (nbd)
    char command[100];
    snprintf(command, sizeof(command), "qemu-nbd --connect=/dev/nbd0 %s", image_path);
    if (system(command) != 0) {
        fprintf(stderr, "Error: Failed to connect qcow2 image to nbd device\n");
        exit(EXIT_FAILURE);
    }

    // Mount the nbd device to the mount point
    if (mount("/dev/nbd0", mount_point, "ext4", 0, "") != 0) {
        fprintf(stderr, "Error: Failed to mount nbd device\n");
        exit(EXIT_FAILURE);
    }

    printf("Qcow2 image mounted at %s\n", mount_point);

    // Optionally, perform operations on the mounted filesystem

    // // Unmount the mounted filesystem
    // if (umount(mount_point) != 0) {
    //     fprintf(stderr, "Error: Failed to unmount filesystem\n");
    //     exit(EXIT_FAILURE);
    // }

    // // Disconnect the nbd device
    // if (system("qemu-nbd --disconnect /dev/nbd0") != 0) {
    //     fprintf(stderr, "Error: Failed to disconnect nbd device\n");
    //     exit(EXIT_FAILURE);
    // }

    // printf("Qcow2 image unmounted\n");

    return 0;
}
