import socket
from threading import Thread
import pickle

def get_weigth_percentage(initial_weight, final_weight):
    weigth_percentage = ((final_weight - initial_weight) / initial_weight) * 100
    return weigth_percentage

def handleConnection(server_socket, clients):
    reply = server_socket.recv(1024)
    data_tuple = pickle.loads(reply)

    initial_weight, final_weight = data_tuple

    initial_weight = float(initial_weight)
    final_weight = float(final_weight)

    result = get_weigth_percentage(initial_weight, final_weight)

    if result >= 0:
        message = f"You had a gain of {result}% of your weigth"
    else:
        message = f"You had a loss of {result * -1}% of your weigth"

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
