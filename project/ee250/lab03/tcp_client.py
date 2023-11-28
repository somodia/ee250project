"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    HOST = "127.0.0.1"
    PORT = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4, TCP protocol
    s.connect((HOST, PORT))
    # TODO: Get user input and send it to the server using your TCP socket
    try: 
        msg = input("What is your message? ").encode()
        s.send(msg)
    # TODO: Receive a response from the server and close the TCP connection
        response = s.recv(255).decode()
        print(f"received {response}")
    finally:
        s.close()
if __name__ == '__main__':
    main()
