import pytest

from urls import BASE_URL


@pytest.fixture
def setup_driver(driver):
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
