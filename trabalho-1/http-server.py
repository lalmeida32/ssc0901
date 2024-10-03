import socket


def create_server(host='localhost', port=8080):
    # Cria um socker TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f'Serving on http://{host}:{port}')

        while True:
            # Aceita uam conexão
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f'Connection from {addr}')
                # Recebe a requisição
                request = client_socket.recv(1024).decode()
                print(f'Request:\n{request}')

                # Prepara uma reposta HTTP
                http_response = """\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Simple HTTP Server</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple HTTP server written in Python.</p>
</body>
</html>
"""
                # Envia a resposta
                client_socket.sendall(http_response.encode())


if __name__ == '__main__':
    create_server()
