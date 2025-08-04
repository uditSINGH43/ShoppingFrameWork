from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def reviewpage(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "name").send_keys("Udit")
    driver.find_element(By.ID, "email").send_keys("xeno12@gmail.com")
    review_box = driver.find_element(By.CSS_SELECTOR, "#review")
    review_box.send_keys("ya very good product but im tired right now...zzz")
    driver.find_element(By.CSS_SELECTOR, "#button-review").click()  # clicking on submit button

    # asserting the thanks button
    message_box = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div[class='col-md-12 form-group'] div[class='alert-success alert']")))
    assert "Thank you for your review." in message_box.text
