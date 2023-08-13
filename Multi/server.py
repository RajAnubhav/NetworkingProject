import threading
import socket

def handle_client(client, nickname, server_index):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, nickname, server_index)
        except:
            index = server_index * max_clients_per_server + clients_per_server[server_index].index(client)
            clients_per_server[server_index].remove(client)
            client.close()
            broadcast(f'{nickname} left the chat!'.encode('ascii'), nickname, server_index)
            nicknames_per_server[server_index].remove(nickname)
            break

def broadcast(message, sender_nickname, server_index):
    for client, nickname in zip(clients_per_server[server_index], nicknames_per_server[server_index]):
        if nickname != sender_nickname:
            client.send(message)

def start_server(host, port, server_index):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames_per_server[server_index].append(nickname)
        clients_per_server[server_index].append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'), nickname, server_index)
        client.send('Connected to the server!'.encode('ascii'))

        client_thread = threading.Thread(target=handle_client, args=(client, nickname, server_index))
        client_thread.start()

servers = [
    ("127.0.0.1", 55555),
    ("127.0.0.1", 55556),
    # Add more servers as needed
]

max_clients_per_server = 10
clients_per_server = [[] for _ in servers]
nicknames_per_server = [[] for _ in servers]

# Start servers in separate threads
server_threads = []
for server_index, server in enumerate(servers):
    host, port = server
    server_thread = threading.Thread(target=start_server, args=(host, port, server_index))
    server_thread.start()
    server_threads.append(server_thread)

# Wait for all server threads to complete
for server_thread in server_threads:
    server_thread.join()

print('Server is listening...')
