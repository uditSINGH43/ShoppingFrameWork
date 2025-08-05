from selenium.webdriver.common.by import By

from On_time_signup.test_cart_addition import cart_add
from On_time_signup.test_payment_page import payment
from On_time_signup.test_verify import verify_details
from Sign_in_page.test_SignUp import signUp
from Sign_in_page.test_account_delete import acc_delete
from Sign_in_page.test_sign2 import personal_info


def test_INvoice(browserInstance):
    invoice_download(browserInstance)


def invoice_download(driver):
    # 1. verify home page

    assert "Automation Exercise" in driver.title

    # 2. adding items to cart
    cart_add(driver)

    # 3. login sequence
    driver.find_element(By.CSS_SELECTOR, "a[href= '/login'] u").click()
    signUp(driver)

    # 3. create account by filling details
    personal_info(driver)

    # 4. verify logged in
    log_user = driver.find_element(By.CSS_SELECTOR, "header[id='header'] li:nth-child(10)")  # verify login part
    assert "Logged in as Udit Singh" == log_user.text.strip()

    # 5. clicking on cart button and proceeding to checkout
    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()

    # 6. verify address details
    verify_details(driver)

    # 7. message box
    driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys("im so close...zzz")
    driver.find_element(By.CSS_SELECTOR, "a[href = '/payment']").click()  # checkout button

    # 8. payment and successfully placing order
    payment(driver)

    # 9. download invoice
    driver.find_element(By.XPATH, "//a[normalize-space()= 'Download Invoice']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    # 10. delete account
    acc_delete(driver)
