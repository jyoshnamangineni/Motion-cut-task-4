# Import necessary modules
import string
import random

# Function to generate a random password of a specified length
def generate_password(length=12):
    # Define the character set including uppercase letters, lowercase letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by selecting random characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    # Return the generated password
    return password

# Function to generate multiple passwords
def generate_multiple_passwords(num_passwords=5, length=12):
    # Generate a list of passwords using the generate_password function
    passwords = [generate_password(length) for _ in range(num_passwords)]
    # Return the list of generated passwords
    return passwords

# Main program
if __name__ == "__main__":
    try:
        # Prompt the user to enter the desired password length and number of passwords
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        # Handle the case where the user enters non-numeric values
        print("Invalid input. Please enter valid numbers.")
        exit(1)

    # Check if entered values are positive
    if password_length <= 0 or num_passwords <= 0:
        print("Please enter valid positive numbers for password length and number of passwords.")
        exit(1)

    # Generate multiple passwords based on user input
    passwords = generate_multiple_passwords(num_passwords, password_length)

    # Display the generated passwords
    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")
