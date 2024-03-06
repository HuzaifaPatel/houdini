houdini: main.o client.o
	gcc -o houdini main.c client.c client.h
clean:
	rm *.o houdini
