import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Login_in.test_loginPage import login


def test_searchProducts(browserInstance):
    searched(browserInstance)


def searched(driver):
    wait = WebDriverWait(driver, 10)

    # going to product section
    product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/products']")))
    product.click()

    # assert to verify if navigated properly
    assert "ALL PRODUCTS" in driver.find_element(By.CSS_SELECTOR, ".title.text-center").text

    # searching through search box by sending keys to find product
    driver.find_element(By.ID, "search_product").send_keys("T-Shirt")
    driver.find_element(By.ID, "submit_search").click()

    # traverse to find items after search
    product_name = driver.find_elements(By.CSS_SELECTOR, ".features_items .col-sm-4")
    expected_names = []

    for item in product_name:
        product_item = item.find_element(By.TAG_NAME, "p").text
        assert re.search(r"t[\s\-]?shirt", product_item.lower())
        expected_names.append(product_item)

    # Step 5: Add all search result items to cart
    for i in range(len(product_name)):
        # Re-fetch the product card each time to avoid stale element reference
        product_card = driver.find_elements(By.CSS_SELECTOR, ".features_items .col-sm-4")[i]
        add_to_cart = product_card.find_element(By.CSS_SELECTOR, ".btn.btn-default.add-to-cart")
        add_to_cart.click()

        # Wait for modal and click Continue
        wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
        continue_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")))
        continue_btn.click()

        time.sleep(1)  # Small delay to stabilize

    # Step 6: Go to cart
    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
    cart_table = wait.until(EC.presence_of_element_located((By.ID, "cart_info_table")))
    rows = cart_table.find_elements(By.TAG_NAME, "tr")
    cart_names = []

    for row in rows:
        try:
            name = row.find_element(By.CSS_SELECTOR, "td.cart_description h4").text.strip()
            cart_names.append(name)
        except:
            continue  # ignore rows without product info

    # Step 7: Check if all added products exist in the cart
    for name in expected_names:
        assert name in cart_names, f"{name} not found in cart"

    # step 8: going to Log_in sequence
    driver.find_element(By.CSS_SELECTOR, "a[class='btn btn-default check_out']").click()
    driver.find_element(By.CSS_SELECTOR, ".text-center u").click()
    login(driver)

    # step 9: again verify cart after login
    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
    cart_table = wait.until(EC.presence_of_element_located((By.ID, "cart_info_table")))
    rows = cart_table.find_elements(By.TAG_NAME, "tr")
    cart_names_after_login = []

    for row in rows:
        try:
            name = row.find_element(By.CSS_SELECTOR, "td.cart_description h4").text.strip()
            cart_names_after_login.append(name)
        except:
            continue

    for name in expected_names:
        assert name in cart_names_after_login, f"{name} not found in cart after login"
