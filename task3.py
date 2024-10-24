import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 8)

    
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    password_length = int(input("Enter the desired password length (minimum 8): "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

    
    