import os
import threading
import time
import random
from typing import Optional

from database import DatabaseManager
from network import Client, Server
from utils import TerminalHelper
from security import security_manager

class D4RK5OCK3T:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.terminal = TerminalHelper()
        self.current_server = None
        self.current_server_thread = None
        self.server_connection_id = None

    def start_server(self, host: str = '0.0.0.0', port: int = 5000):
        """Start the chat server"""
        if not self.current_server:
            server = Server(host, port)
            self.current_server = server
            # Generate connection ID for this server
            self.server_connection_id = security_manager.encode_address(host, port)
            print(f"\n\033[92mConnection ID: {self.server_connection_id}\033[0m")
            print("\033[93mShare this Connection ID with users to let them join.\033[0m")
            server.start()

    def _handle_server_start(self):
        """Handle server start menu option"""
        if self.current_server:
            print("\n\033[93mServer is already running!\033[0m")
            print(f"\033[92mConnection ID: {self.server_connection_id}\033[0m")
            input("\nPress Enter to continue...")
            return

        local_ip = self.terminal.get_local_ip()
        host = local_ip  # Using local IP by default
        port = random.randint(49152, 65535)  # Using random high port for additional security
        
        try:
            server_thread = threading.Thread(target=self.start_server, args=(host, port))
            server_thread.daemon = True
            self.current_server_thread = server_thread
            server_thread.start()
            time.sleep(1)  # Give server a moment to start
        except Exception as e:
            print(f"\n\033[91mFailed to start server: {e}\033[0m")

        input("\nPress Enter to continue...")

    def _handle_group_creation(self):
        """Handle group creation menu option and auto-join the creator"""
        group_name = input("\nEnter Group Name: ").strip()
        username = input("Enter Your Username: ").strip()
        
        # Create the group
        group_id, join_key = self.db_manager.create_group(group_name)
        
        # Clear screen for better visibility
        self.terminal.clear_screen()
        self.terminal.print_logo()
        
        print("\n\033[92m=== GROUP CREATED SUCCESSFULLY ===\033[0m")
        print("\n\033[97m=== SHARE THESE DETAILS WITH YOUR GROUP MEMBERS ===\033[0m")
        print("\n\033[93mGroup Credentials:\033[0m")
        print(f"\033[96mGroup ID: \033[97m{group_id}\033[0m")
        print(f"\033[96mJoin Key: \033[97m{join_key}\033[0m")
        
        try:
            # Start server if not already running
            if not self.current_server:
                local_ip = self.terminal.get_local_ip()
                port = random.randint(49152, 65535)
                server_thread = threading.Thread(target=self.start_server, args=(local_ip, port))
                server_thread.daemon = True
                self.current_server_thread = server_thread
                server_thread.start()
                time.sleep(1)  # Give server a moment to start
            
            print(f"\n\033[93mConnection Details:\033[0m")
            print(f"\033[96mConnection ID: \033[97m{self.server_connection_id}\033[0m")
            
            print("\n\033[97m============================================\033[0m")
            print("\n\033[93mIMPORTANT: Save these details before proceeding!\033[0m")
            input("\n\033[96mPress Enter when you're ready to join the chat...\033[0m")
            
            print("\n\033[92mConnecting to chat...\033[0m")
            # Get host and port from stored connection ID
            host, port = security_manager.decode_address(self.server_connection_id)
            chat = Client(group_id, username, host, port)
            chat.connect()
            
        except Exception as e:
            print(f"\n\033[91mFailed to start server or join group: {e}\033[0m")
            input("Press Enter to continue...")

    def _handle_group_join(self):
        """Handle group join menu option"""
        group_id = input("Enter Group ID: ").strip()
        join_key = input("Enter Join Key: ").strip()
        
        if self.db_manager.validate_group(group_id, join_key):
            username = input("Enter Your Username: ").strip()
            connection_id = input("Enter Connection ID: ").strip()
            
            try:
                # Decode the connection ID to get actual host and port
                host, port = security_manager.decode_address(connection_id)
                chat = Client(group_id, username, host, port)
                chat.connect()
            except Exception as e:
                print(f"\n\033[91mConnection failed: Invalid connection ID or connection refused\033[0m")
                input("Press Enter to continue...")
        else:
            print("\n\033[91mInvalid Group ID or Join Key!\033[0m")
            input("Press Enter to continue...")

    def main_menu(self):
        """Main menu for Terminal Tribe"""
        self.terminal.clear_screen()
        self.terminal.print_logo()

        while True:
            print("\n\033[95m--- TERMINAL TRIBE MENU ---\033[0m")
            print("\033[96m1. Start Server\033[0m")
            print("\033[96m2. Create New Group\033[0m")
            print("\033[96m3. Join Existing Group\033[0m")
            print("\033[96m4. Exit\033[0m")

            choice = input("\n\033[97mEnter your choice (1-4): \033[0m").strip()

            if choice == '1':
                self._handle_server_start()
            elif choice == '2':
                self._handle_group_creation()
            elif choice == '3':
                self._handle_group_join()
            elif choice == '4':
                print("\n\033[92mGoodbye!\033[0m")
                break
            else:
                print("\n\033[91mInvalid choice. Please try again.\033[0m")
                time.sleep(1)

            self.terminal.clear_screen()
            self.terminal.print_logo()


def main():
    try:
        # Ensure terminal supports colors
        if 'TERM' not in os.environ:
            os.environ['TERM'] = 'xterm-256color'

        app = D4RK5OCK3T()
        app.main_menu()
    except KeyboardInterrupt:
        print("\n\033[93mOperation cancelled by user.\033[0m")
    except Exception as e:
        print(f"\n\033[91mAn unexpected error occurred: {e}\033[0m")
    finally:
        print("\n\033[92mThanks for using D4RK5OCK3T\033[0m")


if __name__ == "__main__":
    main()