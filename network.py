import socket
import threading
from typing import Dict, Optional
from utils import ColorManager

class Client:
    def __init__(self, group_id: str, username: str, host: str = '0.0.0.0', port: int = 5000):
        self.group_id = group_id
        self.username = username
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user_color = ColorManager.get_random_color()

    def connect(self):
        """Establish connection to the chat server"""
        try:
            self.client_socket.connect((self.host, self.port))
            
            # Send group, username, and color info
            connection_info = f"{self.group_id}|{self.username}|{self.user_color}"
            self.client_socket.send(connection_info.encode())

            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

            self.send_messages()
        except Exception as e:
            print(f"\n\033[91mConnection Error: {e}\033[0m")
            input("Press Enter to return to menu...")

    def receive_messages(self):
        """Continuously receive and print messages"""
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    username, color, content = message.split('|', 2)
                    formatted_message = ColorManager.colorize(f"{username}: {content}", color)
                    print(f"\r{formatted_message}\n> ", end='', flush=True)
            except:
                print("\n\033[91mConnection lost.\033[0m")
                break

    def send_messages(self):
        """Allow user to send messages"""
        print("\n\033[92m--- Connected to D4RK5OCK3T Chat ---\033[0m")
        print("Type your messages. Press Ctrl+C to exit.")

        try:
            while True:
                message = input("> ")
                if message.lower() in ['exit', 'quit']:
                    break
                formatted_message = f"{self.username}|{self.user_color}|{message}"
                self.client_socket.send(formatted_message.encode())
        except KeyboardInterrupt:
            print("\n\033[93mExiting chat...\033[0m")
        finally:
            self.client_socket.close()

class Server:
    def __init__(self, host: str = '0.0.0.0', port: int = 5000):
        self.host = host
        self.port = port
        self.clients = {}  # socket to group_id mapping
        self.message_history = {}  # group_id to message list mapping
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def broadcast(self, message: str, group_id: str, sender_socket: Optional[socket.socket] = None):
        """Broadcast message to all clients in the same group"""
        # Store message in history
        if group_id not in self.message_history:
            self.message_history[group_id] = []
        self.message_history[group_id].append(message)
        
        # Send to all clients in group
        for client_socket, client_group in list(self.clients.items()):
            if client_group == group_id and client_socket != sender_socket:
                try:
                    client_socket.send(message.encode())
                except:
                    del self.clients[client_socket]

    def handle_client(self, client_socket: socket.socket):
        """Handle individual client communications"""
        try:
            # Receive group, username, and color info
            connection_info = client_socket.recv(1024).decode()
            group_id, username, color = connection_info.split('|')

            # Store client information
            self.clients[client_socket] = group_id
            print(f"\n{username} joined group {group_id}")

            # Send message history to new client
            if group_id in self.message_history:
                for historic_message in self.message_history[group_id]:
                    try:
                        client_socket.send(historic_message.encode())
                    except:
                        break

            # Broadcast join message
            join_message = f"SYSTEM|{color}|{username} has joined the chat"
            self.broadcast(join_message, group_id)

            while True:
                try:
                    message = client_socket.recv(1024).decode()
                    if message:
                        print(f"Received: {message}")
                        self.broadcast(message, group_id, client_socket)
                    else:
                        raise Exception("Client disconnected")
                except:
                    break

        except Exception as e:
            print(f"Client handling error: {e}")
        finally:
            if client_socket in self.clients:
                group_id = self.clients[client_socket]
                leave_message = f"SYSTEM|{color}|{username} has left the chat"
                del self.clients[client_socket]
                self.broadcast(leave_message, group_id)
            client_socket.close()

    def start(self):
        """Start the chat server"""
        print(f"\033[92m[D4RK5OCK3T] Server started on {self.host}:{self.port}\033[0m")

        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket,)
                )
                client_thread.start()
        except KeyboardInterrupt:
            print("\n\033[93mServer shutting down...\033[0m")
        finally:
            self.server_socket.close()