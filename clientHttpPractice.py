import socket


def connect_to_server():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    # create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to server
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        # Send request
        message = "Hello, This is Deva and How are you doing now."
        client_socket.sendall(message.encode("utf-8"))
        print(f"Sent: {message}")

        # Receive response
        response = client_socket.recv(1024)
        print(f"Received: {response.decode('utf-8')}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close client socket
        client_socket.close()


if __name__ == "__main__":
    connect_to_server()
