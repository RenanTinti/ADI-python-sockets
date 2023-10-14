import socket
import pickle

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 7777))

    expenses = []
    expense = 0.0
    while isinstance(expense, float):
        try:
            expense = float(input("Insert new expense or any text to exit: "))
            expenses.append(expense)
        except:
            break

    serialized_data = pickle.dumps(expenses)

    client_socket.send(serialized_data)

    reply = client_socket.recv(1024).decode("utf-8")
    print("Total expenses with 10% tip: " + reply)
