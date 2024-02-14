import socket,os
from faker import Faker

fake = Faker()
fakename = fake.name()
fakeaddress = fake.address()

socket_server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "127.0.0.1"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print("starting up on {}".format(server_address))
socket_server.bind(server_address)
socket_server.listen(1)

while True:
    connection, client_address = socket_server.accept()

    try:
        print("connection from ", client_address)
        
        while True:
            data = connection.recv(512)
            data_str = data.decode("utf-8")
            print("received " + data_str)

            if data:
                response = "succeed to get message from client =>" + data_str + "."
                connection.sendall(response.encode())
            else:
                # print("no data from ", client_address)
                break
    finally:
        print("closing current connection")
        connection.close()