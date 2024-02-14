import socket,sys
from faker import Faker

fake = Faker()
fakename = fake.name()
fakeaddress = fake.address()

socket_client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "127.0.0.1"
print("connecting to {}".format(server_address))

try:
    socket_client.connect(server_address)
except socket.error as error:
    print(error)
    sys.exit(1)
try:
    inputmessage = input("sending a message to the server side: ")
    message = "input message: " + inputmessage + "\nname: " + fakename + "\naddress: " + fakeaddress
    socket_client.sendall(message.encode())
    socket_client.settimeout(5)
    try:
        while True:
            data = socket_client.recv(512)
            data = data.decode("utf-8")

            if data:
                print("succeed to send a data => " + data + "\n")
            else:
                break
    except(TimeoutError):
        print("timeout")
finally:
    print("closing socket")
    socket_client.close()