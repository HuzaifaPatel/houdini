houdini: houdini.o
	gcc -o houdini houdini.c houdini.h
clean:
	rm *.o houdini
