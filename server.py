from socket import *
import tictactoe

print("  _____ ___ ___   _____ _   ___   _____ ___  ___ ")
print(" |_   _|_ _/ __| |_   _/_\ / __| |_   _/ _ \| __|")
print("   | |  | | (__    | |/ _ \ (__    | || (_) | _| ")
print("   |_| |___\___|   |_/_/ \_\___|   |_| \___/|___|\n")

print("Welcome to Tic Tac Toe!")
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 0)) # Bind socket to random available port
server_socket.listen(1) # List
server_port_num = server_socket.getsockname()[1]
print("The server is listening on port " + str(server_port_num) + "...")




