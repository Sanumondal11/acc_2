# agents/recommendation_agent.py

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from core.database import Database

class RecommendationAgent:
    def __init__(self, db: Database):
        self.db = db

    def recommend(self, customer_id, top_k=3):
        _, customer_embedding = self.db.get_customer(customer_id)
        if customer_embedding is None:
            return []

        products = self.db.get_all_products()
        scores = []
        for product_id, metadata, product_embedding in products:
            sim = cosine_similarity([customer_embedding], [product_embedding])[0][0]
            scores.append((product_id, metadata, sim))

        scores.sort(key=lambda x: x[2], reverse=True)
        return scores[:top_k]
