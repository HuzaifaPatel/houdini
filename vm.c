#include "vm.h"


short int add_file_to_vm() {
    // virt-df -a /var/lib/libvirt/images/lol.qcow2
    // guestfish -a lol.qcow2
    int ret;
    const char *image_path = "lol.qcow2";
    const char *format = "qcow2";
    int64_t size = 1024 * 1024 * 1024; // 20 GB

    guestfs_h *g = guestfs_create();
    // Initialize libguestfs
    if (g == NULL) {
        fprintf(stderr, "Error: Failed to create libguestfs handle\n");
        exit(EXIT_FAILURE);
    }

    // Create a new empty disk image. Terminate with -1
    if (guestfs_disk_create(g, image_path, format, size, -1) == -1) {
        fprintf(stderr, "Error: Failed to create disk image\n");
        guestfs_close(g);
        exit(EXIT_FAILURE);
    }

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