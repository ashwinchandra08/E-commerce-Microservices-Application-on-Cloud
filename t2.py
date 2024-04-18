# import requests

# url = "http://127.0.0.1:5000/register"
# payload = {"username": "aaa", "password": "password"}
# headers = {"Content-Type": "application/json"}

# response = requests.post(url, json=payload, headers=headers)

# print(response.status_code)
# print(response.json())
import os
import requests

JWT_SECRET_KEY = "oXL6CHDkzMmr10O072onLaPyFvFliCXm9DA1843vnSA"
url = "http://127.0.0.1:5002/orders"  # Assuming this is the URL for placing orders
payload = {"product_id": 1, "quantity": 2}
access_token = JWT_SECRET_KEY  # Replace this with your actual JWT token
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"}
print(headers.get('Authorization').split(' ')[1])
response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())

