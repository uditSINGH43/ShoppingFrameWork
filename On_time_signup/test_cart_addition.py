from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def cart_add(driver):

    driver.find_element(By.CSS_SELECTOR, "a[href= '/products']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()
    quantity = driver.find_element(By.ID, "quantity")
    quantity.clear()
    quantity.send_keys("4")
    driver.find_element(By.CSS_SELECTOR, "button[class= 'btn btn-default cart']").click()
    driver.find_element(By.CSS_SELECTOR, ".text-center u").click()
    WebDriverWait(driver, 10)
    assert "Checkout" in driver.title
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()  # checkoout sequence
    driver.find_element(By.CSS_SELECTOR, ".modal-body u").click()