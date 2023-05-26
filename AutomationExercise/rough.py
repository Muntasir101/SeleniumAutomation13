import string
import random


def random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(5))
    domain_name = random.choice(domain)
    email = f"{username}@{domain_name}"
    return email


print(random_email())


def random_string():
    letters = string.ascii_lowercase + string.digits
    random_name = ''.join(random.choice(letters) for _ in range(8))
    string_random = f"{random_name}"
    return random_name


print(random_string())


def random_number():
    return random.randint(100, 1000)


for i in range(3):
    print(random_number())
