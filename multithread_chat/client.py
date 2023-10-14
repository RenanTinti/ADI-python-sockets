import socket
import threading
import tkinter as tk
from tkinter import messagebox

SERVER_HOST = 'localhost'
SERVER_PORT = 12345

client_gui = tk.Tk()
client_gui.title("Client")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

def send_message():
    message = message_entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
    else:
        messagebox.showwarning("Warning", "Please enter a message!")

messages_listbox = tk.Listbox(client_gui, height=15, width=50)
messages_listbox.pack(padx=20, pady=20)

message_entry = tk.Entry(client_gui, width=50)
message_entry.pack(padx=20, pady=10)

send_button = tk.Button(client_gui, text="Send", width=20, command=send_message)
send_button.pack(padx=20, pady=10)

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            messages_listbox.insert(tk.END, message)
        except:
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

client_gui.mainloop()
