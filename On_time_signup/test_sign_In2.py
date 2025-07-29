from selenium.webdriver.common.by import By

from On_time_signup.test_cart_addition import cart_add
from On_time_signup.test_payment_page import payment
from On_time_signup.test_verify import verify_details
from Sign_in_page.test_SignUp import signUp
from Sign_in_page.test_account_delete import acc_delete
from Sign_in_page.test_sign2 import personal_info


def test_sign_in2(browserInstance):
    signIn2(browserInstance)

def signIn2(driver):
    #1. verify title page
    assert "Automation Exercise" in driver.title

    #2. signUp procedure before adding cart
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    signUp(driver)

    #3. creating account
    personal_info(driver)

    #4.adding data in cart
    cart_add(driver)

    #5. verifying address and assert product
    verify_details(driver)

    #6. adding comment in message box
    driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys("damn.. im so tired of this")
    driver.find_element(By.CSS_SELECTOR, "a[href = '/payment']").click()  # checkout button

    #7. payment sequence
    payment(driver)

    #8. account deletion sequence
    acc_delete(driver)


