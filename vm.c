#include <stdio.h>
#include <stdlib.h>
#include <libvirt/libvirt.h>

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