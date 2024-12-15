import sqlite3
import uuid
import hashlib
import os
from typing import Tuple, Optional

class DatabaseManager:
    def __init__(self, db_path: Optional[str] = None):
        if not db_path:
            db_path = os.path.join(
                os.path.expanduser('~'),
                '.terminal_tribe.db'
            )
        
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary database tables"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            group_id TEXT PRIMARY KEY,
            group_name TEXT NOT NULL,
            join_key TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.conn.commit()

    def create_group(self, group_name: str) -> Tuple[str, str]:
        """Create a new group with unique ID and join key"""
        group_id = str(uuid.uuid4())[:8]
        join_key = self._generate_join_key(group_name)

        self.cursor.execute(
            'INSERT INTO groups (group_id, group_name, join_key) VALUES (?, ?, ?)',
            (group_id, group_name, join_key)
        )
        self.conn.commit()

        return group_id, join_key

    def _generate_join_key(self, group_name: str) -> str:
        """Generate a secure join key"""
        return hashlib.sha256(
            f"{group_name}{uuid.uuid4()}".encode()
        ).hexdigest()[:8]

    def validate_group(self, group_id: str, join_key: str) -> bool:
        """Validate group exists with given join key"""
        self.cursor.execute(
            'SELECT * FROM groups WHERE group_id = ? AND join_key = ?',
            (group_id, join_key)
        )
        return self.cursor.fetchone() is not None