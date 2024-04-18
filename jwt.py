import os
import jwt
import secrets

# Function to generate a JWT secret key
def generate_jwt_secret_key():
    return secrets.token_urlsafe(32)

# Function to save the JWT secret key to a file
def save_jwt_secret_key(key, filename='jwt_secret_key.txt'):
    with open(filename, 'w') as f:
        f.write(key)

# Function to read the JWT secret key from a file
def read_jwt_secret_key(filename='jwt_secret_key.txt'):
    with open(filename, 'r') as f:
        return f.read()

# Main function
def main():
    # Generate JWT secret key
    jwt_secret_key = generate_jwt_secret_key()

    # Save JWT secret key to file
    save_jwt_secret_key(jwt_secret_key)

    print("JWT secret key generated and saved to 'jwt_secret_key.txt'")

    # Read JWT secret key from file
    stored_jwt_secret_key = read_jwt_secret_key()

    # Print the stored JWT secret key
    print("Stored JWT secret key:", stored_jwt_secret_key)

if __name__ == "__main__":
    main()
