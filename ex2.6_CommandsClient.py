# -*- coding: utf-8 -*-
import socket

def main():
    """
    a client that sends one of four possible commands to a commands server
    """


    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 1729))

    #getting required buffer size from server
    my_socket.send("BufferSize")
    buffersize = my_socket.recv(1024)

    while True:
        command = raw_input("Please Enter one of 4 possible requests: Time, Name, Rand, Exit\n")
        my_socket.send(command)
        reply = my_socket.recv(int(buffersize))
        print reply
        if command == 'Exit':
            my_socket.close()
            break


if __name__ == '__main__':
    main()