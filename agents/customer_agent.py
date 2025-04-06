# agents/customer_agent.py

from core.embedding import generate_embedding
from core.database import Database

class CustomerAgent:
    def __init__(self, db: Database):
        self.db = db

    def update_profile(self, customer_id, profile_text):
        embedding = generate_embedding(profile_text)
        self.db.insert_customer(customer_id, profile_text, embedding)
