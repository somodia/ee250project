1. argc is the number of arguments passed into the program.
    *argv[] is an array of all the inputs.

2. A UNIX File Descriptor is a nonnegative integer that identifies the file. A file descriptor table is an array of integers that represent file descriptors. 

3. A struct groups several variables into one group. sockaddr_in contains a short for address family, unsigned short for address port, sctruct in_addr for address, and a char to set socket address zero

4. socket() returns an int and passes in a short for address family, as well as a stream type.

5. bind() passes in an int and a pointer to sockaddr.
    listen() passes in an int and another int

6. while(1) is used to indicate that the server code will run until it is interrupted. Based on the code, the server may have issues listening to multiple connections and what is coming in, since the code right now only appears to handle one client.

7. The fork() command essentially makes two processes that run the same set of code. In this case, the fork command could be used for each connection to make sure that the server listens to each client and their incoming messages.
