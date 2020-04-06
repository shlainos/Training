# -*- coding: utf-8 -*-
import socket

def main():
    """
    client for an echo server
    """
    massage = raw_input("what would you like to send to the echo server?\n")
    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 1729))
    my_socket.send(massage)
    my_socket.recv(1024)
    my_socket.close()


if __name__ == '__main__':
    main()