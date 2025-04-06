# app/ui.py

import streamlit as st
from core.database import Database
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent

def launch_ui():
    st.set_page_config(page_title="Smart Shopping Agents", layout="centered")
    st.title("🛍️ Smart Shopping AI Agents")

    db = Database()
    customer_agent = CustomerAgent(db)
    product_agent = ProductAgent(db)
    recommender = RecommendationAgent(db)

    tabs = st.tabs(["Customer Profile", "Add Products", "Get Recommendations"])

    with tabs[0]:
        st.header("🧑 Customer Profile")
        customer_id = st.text_input("Customer ID")
        profile = st.text_area("Describe your preferences")
        if st.button("Save Profile"):
            customer_agent.update_profile(customer_id, profile)
            st.success("Profile updated")

    with tabs[1]:
        st.header("📦 Add Product")
        product_id = st.text_input("Product ID")
        metadata = st.text_area("Product Description")
        if st.button("Add Product"):
            product_agent.add_product(product_id, metadata)
            st.success("Product added")

    with tabs[2]:
        st.header("🤖 Recommendations")
        user_id = st.text_input("Enter your Customer ID")
        if st.button("Get Recommendations"):
            results = recommender.recommend(user_id)
            for product_id, metadata, score in results:
                st.write(f"**{product_id}** - {metadata} (Score: {score:.2f})")
