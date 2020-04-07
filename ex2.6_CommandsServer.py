# -*- coding: utf-8 -*-
import socket
import time
import random


def main():
    """
    a commands server that replies to 4 possible commands
    """
    longest_reply = 1024
    buffer_size = 1024
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 1729))
    server_socket.listen(1)
    (client_socket, client_address) = server_socket.accept()

    while True:
        command = client_socket.recv(buffer_size)

        print command

        if command == 'BufferSize':
            reply = str(longest_reply)
        elif command == 'Time':
            reply = 'The time is: ' + time.ctime(time.time())
        elif command == 'Name':
            reply = "My name is Titan"
        elif command == 'Rand':
            reply = 'generated random number is: ' + str(random.randint(1, 10))
        elif command == 'Exit':
            client_socket.send('Terminated session\ngoodbye')
            break
        else:
            reply = 'Unknown command.\nplease try again'
        client_socket.sendall(reply)

        print reply

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()