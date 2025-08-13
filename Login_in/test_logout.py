from selenium.webdriver.common.by import By


def logout(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
