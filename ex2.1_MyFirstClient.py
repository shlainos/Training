# -*- coding: utf-8 -*-
import socket

def main():
    """
    writing a client for an existing server in "networks.cyber.org.il"
    """
    my_socket = socket.socket()
    my_socket.connect(('54.213.229.251', 8820))
    my_socket.send("Barak")
    reply = my_socket.recv(1024)
    print 'the server sent back: ' + reply
    my_socket.close()


if __name__ == '__main__':
    main()