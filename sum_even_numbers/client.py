import socket
import pickle

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 7777))

    start = input("First number: ")
    end = input("Second number: ")

    numbers = (start, end)
    serialized_data = pickle.dumps(numbers)

    client_socket.send(serialized_data)

    reply = client_socket.recv(1024).decode("utf-8")
    print("Sum of all even numbers: " + reply)
