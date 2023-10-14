import socket
import threading
import tkinter as tk

SERVER_HOST = 'localhost'
SERVER_PORT = 12345

server_gui = tk.Tk()
server_gui.title("Server")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

clients = []

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                remove_client(client_socket)
                break
            broadcast("Client {}: {}".format(client_address, message))
            messages_listbox.insert(tk.END, "Client {}: {}".format(client_address, message))
        except:
            remove_client(client_socket)
            break

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def send_message():
    message = server_message_entry.get()
    if message:
        broadcast("Server: " + message)
        messages_listbox.insert(tk.END, "Server: " + message)
    else:
        tk.messagebox.showwarning("Warning", "Please enter a message!")

messages_listbox = tk.Listbox(server_gui, height=15, width=50)
messages_listbox.pack(padx=20, pady=20)

server_message_entry = tk.Entry(server_gui, width=50)
server_message_entry.pack(padx=20, pady=10)

send_button = tk.Button(server_gui, text="Send", width=20, command=send_message)
send_button.pack(padx=20, pady=10)

server_thread = threading.Thread(target=accept_clients)
server_thread.start()

server_gui.mainloop()
