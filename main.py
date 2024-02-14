import socket


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept()
    with connection:
        data = connection.recv(4096)
        connection.send("+PONG\r\n".encode())


if __name__ == "__main__":
    main()
