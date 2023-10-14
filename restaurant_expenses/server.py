import socket
from threading import Thread
import pickle

def calc_expenses(expenses):
    total_expenses = sum(expenses)
    tip = total_expenses * 0.10

    total_expenses_with_tip = total_expenses + tip

    return total_expenses_with_tip

def handleConnection(server_socket, clients):
    reply = server_socket.recv(1024)
    data_list = pickle.loads(reply)

    message = calc_expenses(data_list)
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
