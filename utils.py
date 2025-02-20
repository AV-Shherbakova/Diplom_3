import json
import random
import string

from constants import PASSWORD


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_user_create_str():
    email = generate_random_string(9) + '@mail.ru'
    return json.dumps(get_user_data(email, generate_random_string(6)))


def get_random_index_from_list(items: list):
    max_number = len(items) - 1
    return random.randint(0, max_number)


def get_content_header():
    return {'Content-Type': 'application/json'}


def get_auth_header(token: str):
    return {"Authorization": token}


def get_user_data(email: str, name: str):
    return {
        "name": name,
        "email": email,
        "password": PASSWORD
    }
