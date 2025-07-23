import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_sign2 import personal_info

test_data_path = "C:/Users/Udit Singh/PycharmProjects/PythonProject1/Shopping/test_Shopping.json"

with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]

driver = webdriver.Edge()

driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Udit Singh")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("2004udit@gmail.com")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
wait = WebDriverWait(driver, 2)

personal_info(driver)

driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']").click()
print(driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted'] b").text)
driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

