import json

import pytest
import requests

from constants import ACCESS_TOKEN
from urls import BASE_URL, REGISTER_URL, UPDATE_USER_INFO_URL
from utils import get_content_header, generate_user_create_str, get_auth_header


@pytest.fixture
def setup_driver(driver):
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_and_remove_user():
    register_response = requests.post(REGISTER_URL, headers=get_content_header(), data=generate_user_create_str())
    yield register_response
    delete_body = json.dumps({
        "email": register_response.json().get("email"),
    })
    token = register_response.json().get(ACCESS_TOKEN)
    auth_headers = get_auth_header(token)
    requests.delete(UPDATE_USER_INFO_URL, headers=auth_headers, data=delete_body)
