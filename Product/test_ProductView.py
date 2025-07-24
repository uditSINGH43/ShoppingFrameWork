from selenium.webdriver.common.by import By


def test_product_view(browserInstance):
    product_view(browserInstance)


def product_view(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
    Products_here = driver.find_element(By.CSS_SELECTOR, "h2[class='title text-center']").text
    print(Products_here)
    driver.find_element(By.XPATH, "//a[@href='/product_details/1']").click()

    # varify product name
    assert driver.find_element(By.CSS_SELECTOR, ".product-information h2").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, ".product-information h2").text == "Blue Top"

    # verify product
    assert "Category" in driver.find_element(By.CSS_SELECTOR, ".product-information p").text

    # verify price
    assert "Rs. 500" in driver.find_element(By.CSS_SELECTOR, ".product-information span").text

    # verify other_details
    verify_details = driver.find_element(By.CSS_SELECTOR, ".product-information").text
    assert "Availability: In Stock" in verify_details
    assert "Condition: New" in verify_details
    assert "Brand: Polo" in verify_details
