import socket


def start_Server():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tells the operating system to allow a TCP socket to reuse an address that has just been released by another process (or after it has closed).
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    try:
        # accept connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024)
        if data:
            message = data.decode("utf-8")
            print(f"Received: {message}")

            # Send response
            response = "Message received by server"
            client_socket.send(response.encode("utf-8"))

        client_socket.close()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_Server()
