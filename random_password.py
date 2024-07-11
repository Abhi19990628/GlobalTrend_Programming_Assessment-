import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
print(generate_password())  # Should print a random password
print(generate_password(16))  # Should print a random password of length 16
