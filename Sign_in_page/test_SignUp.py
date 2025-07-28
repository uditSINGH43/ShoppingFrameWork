from selenium.webdriver.common.by import By


def signUp(driver):
    driver.find_element(By.NAME, "name").send_keys("Udit Singh")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa= 'signup-email']").send_keys("2004udit@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa= 'signup-button']").click()