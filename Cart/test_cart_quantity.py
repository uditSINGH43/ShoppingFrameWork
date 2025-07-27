from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_cart_quantity(browserInstance):
    cart_Quantity(browserInstance)


def cart_Quantity(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()
    action = ActionChains(driver)
    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div [class= 'product-information']")))
    # increasing quantity
    prod_quantity = driver.find_element(By.ID, "quantity")
    prod_quantity.clear()
    prod_quantity.send_keys(4)
    action.move_to_element(
        driver.find_element(By.CSS_SELECTOR, "button[class= 'btn btn-default cart']")).click().perform()
    dialog = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div[class='modal-dialog modal-confirm'] p[class='text-center']")))
    dialog_text = dialog.text
    assert "Your product has been added to cart." in dialog_text
    driver.find_element(By.CSS_SELECTOR, "button[class= 'btn btn-success close-modal btn-block']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()

    # verify name and quantity
    product = driver.find_element(By.CSS_SELECTOR, "tr#product-1")

    assert "Blue Top" in product.text
    assert "4" in product.text
