import streamlit as st

st.set_page_config(page_title="AI Fuel Saver", page_icon="⛽")

# --- Login Page ---
def login():
    st.title("🔐 Login to Access AI Fuel Saver")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "user" and password == "1234":
            st.session_state["logged_in"] = True
            st.success("Login successful! 🚀")
        else:
            st.error("Invalid username or password")

# --- Main App ---
def fuel_calculator():
    st.title("⛽ AI Fuel Saver App for Rural Areas")
    st.subheader("Calculate Your Fuel Consumption")

    distance = st.number_input("Enter distance to travel (in km):", min_value=0.0)
    mileage = st.number_input("Enter vehicle mileage (km per litre):", min_value=0.1)
    fuel_price = st.number_input("Enter fuel price (₹ per litre):", min_value=0.0)

    if st.button("Calculate Fuel Cost"):
        fuel_needed = distance / mileage
        total_cost = fuel_needed * fuel_price
        st.success(f"Estimated Fuel Needed: {fuel_needed:.2f} litres")
        st.success(f"Total Fuel Cost: ₹{total_cost:.2f}")

    st.markdown("---")
    st.caption("🚀 Created by *Saloni Ambatkar* | CLC PBL Project 2025")

# --- App Control ---
if "logged_in" not in st.session_state:
    login()
else:
    fuel_calculator()
