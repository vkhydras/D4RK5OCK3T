import base64
import hashlib
import os
import random
import string
from typing import Tuple

class SecurityManager:
    def __init__(self):
        self._host_key = "D4RK5OCK37_SECURE_KEY"  # Fixed key for consistent encoding/decoding
        
    def encode_address(self, host: str, port: int) -> str:
        """Encode host address into an connection string"""
        # Create the connection info
        connection_info = f"{host}:{port}"
        
        # Encrypt connection info
        return self._encrypt_connection_info(connection_info)
    
    def decode_address(self, connection_id: str) -> Tuple[str, int]:
        """Decode a connection string back to host and port"""
        try:
            connection_info = self._decrypt_connection_info(connection_id)
            host, port = connection_info.split(':')
            return host, int(port)
        except:
            raise ValueError("Invalid connection ID")
    
    def _encrypt_connection_info(self, connection_info: str) -> str:
        """Encrypt connection information"""
        key = hashlib.sha256(self._host_key.encode()).digest()
        # XOR encryption with key
        encrypted = []
        for i, c in enumerate(connection_info.encode()):
            encrypted.append(c ^ key[i % len(key)])
        return base64.b85encode(bytes(encrypted)).decode()
    
    def _decrypt_connection_info(self, encrypted: str) -> str:
        """Decrypt connection information"""
        key = hashlib.sha256(self._host_key.encode()).digest()
        encrypted_bytes = base64.b85decode(encrypted.encode())
        # XOR decryption with key
        decrypted = []
        for i, c in enumerate(encrypted_bytes):
            decrypted.append(c ^ key[i % len(key)])
        return bytes(decrypted).decode()

# Global security manager instance
security_manager = SecurityManager()