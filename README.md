# E-commerce Microservices
#recent change
This project demonstrates a simple e-commerce system built using a microservices architecture. It consists of three main services:
#trying change from ananya system 
1. **User Authentication Service**: Handles user registration and login, providing JWT tokens for authenticated sessions.
2. **Product Management Service**: Manages product information, including creation, updates, and retrieval of product details.
3. **Order Processing Service**: Manages orders, including placing new orders and retrieving user order history.

## Technology Stack

- Backend: Streamlit
- Database: SQLite for simplicity and demonstration purposes (can be replaced with any SQL database)
- Authentication: JWT


### Prerequisites

- Python 3.12+
- Docker and Docker Compose (optional, for containerized deployment), Kubernetes



The services can be accessed at the following URLs when running locally:

- User Authentication Service: `http://localhost:5001`
- Product Management Service: `http://localhost:5002`
- Order Processing Service: `http://localhost:5003`

## API Endpoints

### User Authentication Service

- **Register a User**
  - POST `/register`
  - Payload: `{"username": "testuser", "password": "password"}`

- **Log In**
  - POST `/login`
  - Payload: `{"username": "testuser", "password": "password"}`
  - Response: `{"access_token": "<JWT_Token>"}`

### Product Management Service

- **Create a Product** (Authenticated)
  - POST `/products`
  - Headers: `Authorization: Bearer <JWT_Token>`
  - Payload: `{"name": "New Product", "description": "Product Description", "price": 99.99, "quantity": 100}`

- **Get All Products** (Authenticated)
  - GET `/products`

- **Get a Single Product** (Authenticated)
  - GET `/products/<product_id>`

- **Update a Product** (Authenticated)
  - PUT `/products/<product_id>`
  - Headers: `Authorization: Bearer <JWT_Token>`
  - Payload: `{"name": "Updated Product", "description": "Updated Description", "price": 89.99, "quantity": 150}`

- **Delete a Product** (Authenticated)
  - DELETE `/products/<product_id>`
  - Headers: `Authorization: Bearer <JWT_Token>`

### Order Processing Service

- **Place an Order** (Authenticated)
  - POST `/orders`
  - Headers: `Authorization: Bearer <JWT_Token>`
  - Payload: `{"product_id": 1, "quantity": 2}`

- **Get User Orders** (Authenticated)
  - GET `/orders`
  - Headers: `Authorization: Bearer <JWT_Token>`

### Example Requests

1. **Register a User**

POST `http://localhost:5001/register`

Payload:

```json
{
    "username": "testuser",
    "password": "password"
}
```

2. **Log In**

POST `http://localhost:5001/login`

Payload:

```json
{
    "username": "testuser",
    "password": "password"
}
```

3. **Create a Product** (as an authenticated user)

POST `http://localhost:5002/products`

Headers:

```
Authorization: Bearer <JWT_Token>
```

Payload:

```json
{
    "name": "New Product",
    "description": "Product Description",
    "price": 99.99,
    "quantity": 100
}
```

4. **Place an Order** (as an authenticated user)

POST `http://localhost:5003/orders`

Headers:

```
Authorization: Bearer <JWT_Token>
```

Payload:

```json
{
    "product_id": 1,
    "quantity": 2
}
```
## NOTE: TEMPORARY PORT FORWARDING

	kubectl port-forward service/<service-name> <local-port>:<remote-port>
 
 	RUN THIS:
	kubectl port-forward service/user-auth 5001:5001
  
	kubectl port-forward service/product-management 5002:5002
