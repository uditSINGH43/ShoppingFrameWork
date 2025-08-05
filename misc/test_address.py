from selenium.webdriver.common.by import By

from On_time_signup.test_cart_addition import cart_add
from On_time_signup.test_verify import verify_details
from Sign_in_page.test_SignUp import signUp
from Sign_in_page.test_account_delete import acc_delete
from Sign_in_page.test_sign2 import personal_info
from conftest import browserInstance


def test_address(browserInstance):
    addressPage(browserInstance)


def addressPage(driver):
    # 1. verify home page

    assert "Automation Exercise" in driver.title

    # 2. signup to create account
    driver.find_element(By.CSS_SELECTOR, "a[href= '/login']").click()
    signUp(driver)

    # 3. create account by filling details
    personal_info(driver)

    # 4. adding product to cart
    cart_add(driver)

    # 5. asserting address this file has same address as time of signup...
    verify_details(driver)

    # 6. account delete
    acc_delete(driver)
