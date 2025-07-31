from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_delCart(browserInstance):
    deletecart(browserInstance)

def deletecart(driver):
    assert "Automation Exercise" in driver.title

    driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()
    cart_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class= 'btn btn-default cart']")))
    cart_button.click()
    Add_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class= 'btn btn-default cart']")))
    Add_button.click()
    driver.find_element(By.CSS_SELECTOR, ".text-center a").click()
    assert "Checkout" in driver.title
    driver.find_element(By.CSS_SELECTOR, ".cart_quantity_delete").click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".text-center b"), "Cart is empty!"))
    assert "Cart is empty!" in driver.find_element(By.CSS_SELECTOR, ".text-center b").text
