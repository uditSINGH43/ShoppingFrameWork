from selenium.webdriver.common.by import By


def payment(driver):
    # payment page
    driver.find_element(By.NAME, "name_on_card").send_keys("Udit Singh")
    driver.find_element(By.CSS_SELECTOR, "input[name= 'card_number']").send_keys("142678")
    driver.find_element(By.NAME, "cvc").send_keys("666")
    driver.find_element(By.NAME, "expiry_month").send_keys("09")
    driver.find_element(By.NAME, "expiry_year").send_keys("3026")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='pay-button']").click()
    placed = driver.find_element(By.CSS_SELECTOR, "div.col-sm-9.col-sm-offset-1 > p").text
    assert "Congratulations! Your order has been confirmed!" in placed.strip()
