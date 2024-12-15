import os
import socket
import time
import random
from typing import Tuple, List

class ColorManager:
    COLORS = [
        '\033[38;5;{}m'.format(i) for i in range(1, 255)
        if i not in [0, 7, 8, 15, 16]  # Excluding blacks, whites, and grays
    ]
    RESET = '\033[0m'
    
    @classmethod
    def get_random_color(cls) -> str:
        return random.choice(cls.COLORS)
    
    @classmethod
    def colorize(cls, text: str, color: str) -> str:
        return f"{color}{text}{cls.RESET}"

class TerminalHelper:
    @staticmethod
    def clear_screen():
        """Cross-platform screen clear"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_logo():
        """Display D4RK5OCK37 logo"""
        logo = [
            r"  _____  _  _      ____  _  __  ____   ___   ____ _  __ ____  _____ ",
            r" |  __ \| || |    |  _ \| |/ / | ___| / _ \ / ___| |/ /|___ \|___  |",
            r" | |  | | || |_   | |_) | ' /  |___ \| | | | |   | ' /   __) |  / / ",
            r" | |  | |__   _|  |  _ <| . \   ___) | |_| | |___| . \  / __/  / /  ",
            r" | |__| |  | |    | |_) | |\  \ |____/ \___/ \____|_|\_\|_____|/ /   ",
            r" |_____/   |_|    |____/|_| \_\               |_____/        |___/    "
        ]

        colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
        reset = '\033[0m'

        for i, line in enumerate(logo):
            color = colors[i % len(colors)]
            print(f"{color}{line}{reset}")
            time.sleep(0.1)

        print("\n\033[92mSecure. Anonymous. Connected.\033[0m")

    @staticmethod
    def get_local_ip() -> str:
        """Get the local IP address"""
        try:
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            temp_socket.connect(("8.8.8.8", 80))
            local_ip = temp_socket.getsockname()[0]
            temp_socket.close()
            return local_ip
        except:
            return '127.0.0.1'