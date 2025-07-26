from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_cart(browserInstance):
    cart(browserInstance)

def cart(driver):
    action = ActionChains(driver)
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']")).click().perform()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default cart']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/2']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default cart']").click()
    Cart_click = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    action.move_to_element(Cart_click).click().perform()
    product_1 = driver.find_element(By.CSS_SELECTOR, "tr#product-1")
    product_2 = driver.find_element(By.CSS_SELECTOR, "tr#product-2")

    #for product_1

    assert "Blue Top" in product_1.text
    assert "Rs. 500" in product_1.text
    assert "1" in product_1.text

    #for product_2
    assert "Men Tshirt" in product_2.text
    assert "Rs. 400" in product_2.text
    assert "1" in product_2.text

    # Optional: Verify total prices if needed
    total1 = product_1.find_element(By.CLASS_NAME, "cart_total").text
    total2 = product_2.find_element(By.CLASS_NAME, "cart_total").text
    assert "Rs. 500" in total1
    assert "Rs. 400" in total2






