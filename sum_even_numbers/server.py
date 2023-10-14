import socket
from threading import Thread
import pickle

def sum_even_numbers(start, end):
    if start > end:
        start, end = end, start

    total_sum = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num

    return total_sum

def handleConnection(server_socket, clients):
    reply = server_socket.recv(1024)
    data_tuple = pickle.loads(reply)

    start, end = data_tuple
    start = int(start)
    end = int(end)

    message = sum_even_numbers(start, end)
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
