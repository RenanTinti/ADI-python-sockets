import socket
from threading import Thread
import pickle

def calc_new_price(price):
    price_raised = price * 0.25
    new_price = price + price_raised
    return new_price

def handleConnection(server_socket, clients):
    reply = server_socket.recv(1024)
    data_float = pickle.loads(reply)

    message = calc_new_price(data_float)
    server_socket.send(str(message).encode("utf-8"))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 7777))
server_socket.listen(5)
clients = 0

while True:
    clients += 1
    message, address = server_socket.accept()
    thread = Thread(target=handleConnection, args=(message, clients))
    thread.start()
