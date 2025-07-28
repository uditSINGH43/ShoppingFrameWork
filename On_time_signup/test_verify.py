from selenium.webdriver.common.by import By


def verify_details(driver):
    actual_address = [li.text.strip() for li in driver.find_elements(By.CSS_SELECTOR, "ul.address.item.box li")]
    expected_address = ["YOUR DELIVERY ADDRESS",
                        "Mr. Udit Singh",
                        "Fresher",
                        "Gandhi Nagar",
                        "that's it",
                        "Aligarh Uttar Pradesh 202001",
                        "India",
                        "9258192581"]
    assert actual_address == expected_address  # address assertion
    product_1 = driver.find_element(By.CSS_SELECTOR, "tr#product-1")  # product asertion
    assert "Blue Top" in product_1.text
    assert "4" in product_1.text