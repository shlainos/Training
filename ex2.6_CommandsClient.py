# -*- coding: utf-8 -*-
import socket

def main():
    """
    a client that sends one of four possible commands to a commands server
    """
    end_flag = '/fin'

    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 1729))

    #getting required buffer size from server
    my_socket.send("BufferSize" + end_flag)
    buffersize = my_socket.recv(1024)

    while True:
        raw_command = raw_input("Please Enter one of 4 possible requests: Time, Name, Rand, Exit\n")
        command = raw_command + end_flag
        my_socket.send(command)
        reply = my_socket.recv(int(buffersize))
        print reply
        if raw_command == 'Exit':
            my_socket.close()
            break


if __name__ == '__main__':
    main()