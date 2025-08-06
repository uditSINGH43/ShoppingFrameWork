import os
from selenium import webdriver
import pytest

driver = None  # This is your global driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Edge", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "Edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(5)
    driver.get("https://automationexercise.com/")
    yield driver
    driver.quit()  # better than close

