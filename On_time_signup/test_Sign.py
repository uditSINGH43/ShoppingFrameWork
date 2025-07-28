from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from On_time_signup.test_payment_page import payment
from On_time_signup.test_verify import verify_details
from Sign_in_page.test_SignUp import signUp
from Sign_in_page.test_sign2 import personal_info


def test_SignIn(browserInstance):
    SignUp(browserInstance)


def SignUp(driver):
    assert "Automation Exercise" in driver.title
    # Adding items in cart

    driver.find_element(By.CSS_SELECTOR, "a[href= '/products']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()
    quantity = driver.find_element(By.ID, "quantity")
    quantity.clear()
    quantity.send_keys("4")
    driver.find_element(By.CSS_SELECTOR, "button[class= 'btn btn-default cart']").click()
    driver.find_element(By.CSS_SELECTOR, ".text-center u").click()
    WebDriverWait(driver, 10)
    assert "Checkout" in driver.title
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()  # checkoout sequence
    driver.find_element(By.CSS_SELECTOR, ".modal-body u").click()

    # SignUp
    signUp(driver)

    # call personal info detail from another file
    personal_info(driver)
    log_user = driver.find_element(By.CSS_SELECTOR, "header[id='header'] li:nth-child(10)")#verify login part
    assert "Logged in as Udit Singh" == log_user.text.strip()

    #entering cart and checking out
    driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()

    #verify address and cart details
    verify_details(driver)

    #message box
    driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys("damn.. im so tired of this")
    driver.find_element(By.CSS_SELECTOR, "a[href = '/payment']").click() #checkout button

    #payment
    payment(driver)



