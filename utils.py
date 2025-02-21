import json
import random
import string

import requests
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.webdriver import WebDriver

from browser import Browser
from constants import PASSWORD, ACCESS_TOKEN, ID
from urls import INGREDIENTS_URL, ORDER_URL


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


def get_ingredients_response():
    return requests.get(INGREDIENTS_URL, headers=get_content_header())


def create_order_and_get_field(create_response: Response, field: str):
    ingredient_response = get_ingredients_response()
    ingredients: list = ingredient_response.json().get('data')
    ingredient1 = ingredients[0]
    ingredient2 = ingredients[1]
    ingredient_ids = [ingredient1.get(ID), ingredient2.get(ID)]
    order_data = {
        "ingredients": ingredient_ids
    }
    token = create_response.json().get(ACCESS_TOKEN)
    auth_headers = get_auth_header(token)
    order_response = requests.post(ORDER_URL, headers=auth_headers, json=order_data)
    return order_response.json().get('order').get(field)


def get_driver(browser: Browser) -> WebDriver:
    return webdriver.Firefox(options=get_options(browser)) \
        if browser == Browser.FIREFOX \
        else \
        webdriver.Chrome(options=get_options(browser))


def get_options(browser: Browser):
    if browser == Browser.FIREFOX:
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.set_preference("layout.css.devPixelsPerPx", "0.8")
        return options
    else:
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--force-device-scale-factor=0.8")
        return options
