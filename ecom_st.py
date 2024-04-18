import streamlit as st
import requests

# Base URLs for each service
AUTH_BASE_URL = "http://127.0.0.1:5001"  #"http://localhost:5000"
PRODUCT_BASE_URL = "http://127.0.0.1:5002"
ORDER_BASE_URL = "http://127.0.0.1:5003"

# Function to register a user
# def register_user(username, password):
#     response = requests.post(f"{AUTH_BASE_URL}/register", json={"username": username, "password": password})
#     print(response)
#     return response.json()
def register_user(username, password):
    url = "http://127.0.0.1:5000/register"
    payload = {"username": username, "password": password}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response

# Function to log in a user
def login_user(username, password):
    response = requests.post(f"{AUTH_BASE_URL}/login", json={"username": username, "password": password})
    return response.json()

# Function to create a product
def create_product(token, name, description, price, quantity):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": name, "description": description, "price": price, "quantity": quantity}
    response = requests.post(f"{PRODUCT_BASE_URL}/products", headers=headers, json=payload)
    return response.json()

# Function to get all products
def get_all_products(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{PRODUCT_BASE_URL}/products", headers=headers)
    return response.json()

# Function to get a single product
def get_single_product(token, product_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{PRODUCT_BASE_URL}/products/{product_id}", headers=headers)
    return response.json()

# Function to update a product
def update_product(token, product_id, name, description, price, quantity):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": name, "description": description, "price": price, "quantity": quantity}
    response = requests.put(f"{PRODUCT_BASE_URL}/products/{product_id}", headers=headers, json=payload)
    return response.json()

# Function to delete a product
def delete_product(token, product_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{PRODUCT_BASE_URL}/products/{product_id}", headers=headers)
    return response.json()

# Function to place an order
def place_order(token, product_id, quantity):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"product_id": product_id, "quantity": quantity}
    response = requests.post(f"{ORDER_BASE_URL}/orders", headers=headers, json=payload)
    print(response)
    return response.json()
def get_user_orders(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{ORDER_BASE_URL}/orders", headers=headers)
    print(response)
    return response.json()

# Main function to run the Streamlit app
def main():
    st.title("E-Commerce Management System")

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ["Register", "Login", "Create Product", "Get All Products", "Get Single Product", "Update Product", "Delete Product", "Place Order","Get All Orders"])

    if page == "Register":
        st.header("Register")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            response = register_user(username, password)
            st.write(response)

    elif page == "Login":
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            response = login_user(username, password)
            st.write(response)
            if "access_token" in response:
                st.session_state.token = response["access_token"]

    elif page == "Create Product":
        st.header("Create Product")
        if "token" not in st.session_state:
            st.warning("Please log in to create a product.")
        else:
            token = st.session_state.token
            name = st.text_input("Name")
            description = st.text_input("Description")
            price = st.number_input("Price", value=0.0)
            quantity = st.number_input("Quantity", value=0)
            if st.button("Create Product"):
                response = create_product(token, name, description, price, quantity)
                st.write(response)

    elif page == "Get All Products":
        st.header("Get All Products")
        if "token" not in st.session_state:
            st.warning("Please log in to get all products.")
        else:
            token = st.session_state.token
            response = get_all_products(token)
            st.write(response)

    elif page == "Get Single Product":
        st.header("Get Single Product")
        if "token" not in st.session_state:
            st.warning("Please log in to get a single product.")
        else:
            token = st.session_state.token
            product_id = st.number_input("Product ID", value=0)
            if st.button("Get Product"):
                response = get_single_product(token, product_id)
                st.write(response)

    elif page == "Update Product":
        st.header("Update Product")
        if "token" not in st.session_state:
            st.warning("Please log in to update a product.")
        else:
            token = st.session_state.token
            product_id = st.number_input("Product ID", value=0)
            name = st.text_input("Name")
            description = st.text_input("Description")
            price = st.number_input("Price", value=0.0)
            quantity = st.number_input("Quantity", value=0)
            if st.button("Update Product"):
                response = update_product(token, product_id, name, description, price, quantity)
                st.write(response)

    elif page == "Delete Product":
        st.header("Delete Product")
        if "token" not in st.session_state:
            st.warning("Please log in to delete a product.")
        else:
            token = st.session_state.token
            product_id = st.number_input("Product ID", value=0)
            if st.button("Delete Product"):
                response = delete_product(token, product_id)
                st.write(response)

    elif page == "Place Order":
        st.header("Place Order")
        if "token" not in st.session_state:
            st.warning("Please log in to place an order.")
        else:
            token = st.session_state.token
            product_id = st.number_input("Product ID", value=0)
            quantity = st.number_input("Quantity", value=0)
            if st.button("Place Order"):
                response = place_order(token, product_id, quantity)
                st.write(response)
    elif page == "Get All Orders":
        st.header("Get All Orders")
        if "token" not in st.session_state:
            st.warning("Please log in to get all products.")
        else:
            token = st.session_state.token
            response = get_user_orders(token)
            st.write(response)


if __name__ == "__main__":
    main()
