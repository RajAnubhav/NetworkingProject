import socket
import threading

class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self, host, port):
        self.client.connect((host, port))
        self.client.send(self.nickname.encode('ascii'))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                print(message)
            except:
                print('An error occurred!')
                self.client.close()
                break

    def write(self):
        while True:
            message = input("")
            if message.lower() == "exit":
                self.client.close()
                break
            self.client.send(f'{self.nickname}: {message}'.encode('ascii'))

nickname = input('Choose a nickname: ')

servers = [
    {'name': 'Server 1', 'host': '127.0.0.1', 'port': 55555},
    {'name': 'Server 2', 'host': '127.0.0.1', 'port': 55556},
    # Add more server details as needed
]

# Display available servers
print('Available Servers:')
for i, server in enumerate(servers):
    print(f'{i+1}. {server["name"]} ({server["host"]}:{server["port"]})')

# Prompt user to choose a server
server_choice = input('Enter the server number you want to join: ')
server_choice = int(server_choice) - 1

if server_choice < 0 or server_choice >= len(servers):
    print('Invalid server choice!')
else:
    server = servers[server_choice]
    client = ChatClient(nickname)
    client.connect_to_server(server['host'], server['port'])

    # Start threads for the client
    receive_thread = threading.Thread(target=client.receive)
    receive_thread.start()

    write_thread = threading.Thread(target=client.write)
    write_thread.start()

    # Wait for the threads to complete
    receive_thread.join()
    write_thread.join()
