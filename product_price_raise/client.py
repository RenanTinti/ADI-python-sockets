import socket
import pickle

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 7777))

    while True:
        try:
            price = float(input("Product price ($): "))
            break
        except:
            print("Invalid input. Please enter a valid price.")

    serialized_data = pickle.dumps(price)

    client_socket.send(serialized_data)

    reply = client_socket.recv(1024).decode("utf-8")
    print("New product price with a raise of 25%: $" + reply)
