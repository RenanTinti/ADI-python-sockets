import socket
import pickle

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 7777))

    while True:
        try:
            initial_weight = float(input("Initial weigth: "))
            break
        except:
            print("Invalid input. Please enter a valid weigth.")

    while True:
        try:
            final_weight = float(input("Final weigth: "))
            break
        except:
            print("Invalid input. Please enter a valid weigth.")

    values = (initial_weight, final_weight)
    serialized_data = pickle.dumps(values)

    client_socket.send(serialized_data)

    reply = client_socket.recv(1024).decode("utf-8")
    print(reply)
