# core/database.py

import sqlite3
import json

class Database:
    def __init__(self, db_name='shopping_ai.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id TEXT PRIMARY KEY,
                    profile TEXT,
                    embedding TEXT
                )''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    product_id TEXT PRIMARY KEY,
                    metadata TEXT,
                    embedding TEXT
                )''')

    def insert_customer(self, customer_id, profile, embedding):
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO customers VALUES (?, ?, ?)''',
                (customer_id, profile, json.dumps(embedding)))

    def insert_product(self, product_id, metadata, embedding):
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO products VALUES (?, ?, ?)''',
                (product_id, metadata, json.dumps(embedding)))

    def get_customer(self, customer_id):
        cursor = self.conn.execute('SELECT profile, embedding FROM customers WHERE customer_id = ?', (customer_id,))
        row = cursor.fetchone()
        if row:
            return row[0], json.loads(row[1])
        return None, None

    def get_all_products(self):
        cursor = self.conn.execute('SELECT product_id, metadata, embedding FROM products')
        return [(row[0], row[1], json.loads(row[2])) for row in cursor.fetchall()]
