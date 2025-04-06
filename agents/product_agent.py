# agents/product_agent.py

from core.embedding import generate_embedding
from core.database import Database

class ProductAgent:
    def __init__(self, db: Database):
        self.db = db

    def add_product(self, product_id, metadata):
        embedding = generate_embedding(metadata)
        self.db.insert_product(product_id, metadata, embedding)
