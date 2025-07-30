from selenium.webdriver.common.by import By

#from test_loginPage2 import logout


def login(driver):


    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("2004udit@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("as")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

    #logout(driver)

# THIS is what pytest will recognize and run
def test_login(browserInstance):
    login(browserInstance)





