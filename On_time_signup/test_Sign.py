from selenium.webdriver.common.by import By

from On_time_signup.test_cart_addition import cart_add
from On_time_signup.test_payment_page import payment
from On_time_signup.test_verify import verify_details
from Sign_in_page.test_SignUp import signUp
from Sign_in_page.test_sign2 import personal_info


def test_SignIn(browserInstance):
    SignUp(browserInstance)


def SignUp(driver):
    assert "Automation Exercise" in driver.title
    # Adding items in cart
    cart_add(driver)

    # SignUp
    signUp(driver)

    # call personal info detail from another file
    personal_info(driver)
    log_user = driver.find_element(By.CSS_SELECTOR, "header[id='header'] li:nth-child(10)")  # verify login part
    assert "Logged in as Udit Singh" == log_user.text.strip()

    # entering cart and checking out
    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()

    # verify address and cart details
    verify_details(driver)

    # message box
    driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys("damn.. im so tired of this")
    driver.find_element(By.CSS_SELECTOR, "a[href = '/payment']").click()  # checkout button

    # payment
    payment(driver)

    # delete account
    driver.find_element(By.CSS_SELECTOR, "a[href= '/delete_account']").click()
    delete_account = driver.find_element(By.CSS_SELECTOR, "h2[data-qa= 'account-deleted']").text
    assert "ACCOUNT DELETED!" in delete_account.strip()
