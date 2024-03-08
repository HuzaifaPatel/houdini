#include "vm.h"

short int make_qcow2(){
    FILE *file = fopen("lol.qcow2", "r");
    if (file != NULL) {
        printf("Qcow2 image already exists.\n");
        fclose(file);
        return 0;
    }

    // Define the command to create the qcow2 image
    const char *command = "qemu-img create -f qcow2 lol.qcow2 20G";

    // Execute the command
    int status = system(command);

    if (status == 0) {
        printf("Qcow2 image created successfully.\n");
    } else {
        printf("Failed to create qcow2 image.\n");
    }

    return 0;
}

short int add_file_to_vm() {
    // virt-df -a /var/lib/libvirt/images/lol.xcow2
    // guestfish -a lol.qcow2
    guestfs_h *g;

    make_qcow2();
    g = guestfs_create();
    if (g == NULL) {
        fprintf(stderr, "Failed to create libguestfs handle\n");
        exit(EXIT_FAILURE);
    }

    if (guestfs_add_drive(g, "lol.qcow2") == -1) {
        fprintf(stderr, "Failed to add drive\n");
        guestfs_close(g);
        exit(EXIT_FAILURE);
    }

    if (guestfs_launch(g) == -1) {
        fprintf(stderr, "Failed to launch libguestfs\n");
        guestfs_close(g);
        exit(EXIT_FAILURE);
    }

    if (guestfs_mount(g, "/dev/sda1", "/") == -1) {
        fprintf(stderr, "Failed to mount filesystem\n");
        guestfs_close(g);
        exit(EXIT_FAILURE);
    }

    if (guestfs_upload(g, "main.c", "/main.c") == -1) {
        fprintf(stderr, "Failed to upload file\n");
        guestfs_close(g);
        exit(EXIT_FAILURE);
    }

    if (guestfs_umount_all(g) == -1) {
        fprintf(stderr, "Failed to unmount filesystem\n");
        guestfs_close(g);
        exit(EXIT_FAILURE);
    }

    guestfs_close(g);

    return 0;
}



int get_ip_address() {
    // https://libvirt.org/html/libvirt-libvirt-domain.html#virDomainInterfacePtr
    virDomainInterfacePtr *ifaces = NULL;
    virDomainPtr *domains = NULL;
    int ifaces_count = 0;
    int num_domains;
    int i,j,k;

    // Connect to the hypervisor
    const virConnectPtr conn = virConnectOpen("qemu:///system");
    if (conn == NULL) {
        fprintf(stderr, "Failed to connect to the hypervisor\n");
        return 1;
    }

    num_domains = virConnectListAllDomains(conn, &domains, VIR_CONNECT_LIST_DOMAINS_ACTIVE);

    // Loop through active domains
    for (i = 0; i < num_domains; i++) {
        const virDomainPtr domain = domains[i];
        const char *name = virDomainGetName(domain);
        printf("Domain: %s\n", name);

        if ((ifaces_count = virDomainInterfaceAddresses(domain, &ifaces, VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_LEASE, 0)) < 0)
            goto cleanup;

        for (j = 0; j < ifaces_count; j++) {
            printf("name: %s", ifaces[j]->name);
            if (ifaces[j]->hwaddr)
                printf(" hwaddr: %s", ifaces[j]->hwaddr);

            for (k = 0; k < ifaces[j]->naddrs; k++) {
                virDomainIPAddressPtr ip_addr = ifaces[j]->addrs + k;
                printf("[addr: %s prefix: %d type: %d]",
                       ip_addr->addr, ip_addr->prefix, ip_addr->type);
            }
            printf("\n");
        }
    }

    cleanup:
        if (ifaces && ifaces_count > 0)
            for (i = 0; i < ifaces_count; i++)
                virDomainInterfaceFree(ifaces[i]);
        free(ifaces);


    return 0;
}