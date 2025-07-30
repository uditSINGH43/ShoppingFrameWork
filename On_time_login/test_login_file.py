from selenium.webdriver.common.by import By

from Login_in.test_loginPage import login
from On_time_signup.test_cart_addition import cart_add
from On_time_signup.test_payment_page import payment
from On_time_signup.test_verify import verify_details
from Sign_in_page.test_account_delete import acc_delete


def test_loginPage(browserInstance):
    loginpage(browserInstance)

def loginpage(driver):
    #verify if title page is visible
    assert "Automation Exercise" in driver.title

    #login sequence called from different file
    login(driver)

    #verifying if login successful
    log_user = driver.find_element(By.CSS_SELECTOR, "header[id='header'] li:nth-child(10)")  # verify login part
    assert "Logged in as Udit Singh" == log_user.text.strip()

    #adding product to cart
    cart_add(driver)

    #verify details
    verify_details(driver)

    #message box
    driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys("damn.. im so tired of this")
    driver.find_element(By.CSS_SELECTOR, "a[href = '/payment']").click()  # checkout button

    #payment sequence
    payment(driver)

    #account delete sequence
    acc_delete(driver)







