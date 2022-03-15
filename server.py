from socket import *
import tictactoe

print("  _____ ___ ___   _____ _   ___   _____ ___  ___ ")
print(" |_   _|_ _/ __| |_   _/_\ / __| |_   _/ _ \| __|")
print("   | |  | | (__    | |/ _ \ (__    | || (_) | _| ")
print("   |_| |___\___|   |_/_/ \_\___|   |_| \___/|___|\n")

print("Welcome to Tic Tac Toe!")
client1_socket = socket(AF_INET, SOCK_STREAM)
client2_socket = socket(AF_INET, SOCK_STREAM)
client1_socket.bind(('', 0)) # Bind socket to random available port
client2_socket.bind(('', 0))
client1_socket.listen(1) # Listen to 1 connection at a time...
client2_socket.listen(1)
client1_port_num = client1_socket.getsockname()[1]
client2_port_num = client2_socket.getsockname()[1]
print("The server is listening on port " + str(client1_port_num) + " and port " + str(client2_port_num) + "...")

while True:



