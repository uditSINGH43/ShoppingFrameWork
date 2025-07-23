from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_contact(browserInstance):
    contact(browserInstance)


def contact(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']").click()
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("uditSingh")
    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("2004udit@gmail.com")
    driver.find_element(By.XPATH, "//input[@data-qa='subject']").send_keys("faulty product")
    driver.find_element(By.TAG_NAME, "textarea").send_keys("product is not good, gonna replace it, bill isw attached")
    file_upload = driver.find_element(By.CSS_SELECTOR, "input[name='upload_file']")
    file_upload.send_keys("C:/Users/Udit Singh/Desktop/CV/new.docx")
    driver.find_element(By.XPATH, "//input[@data-qa='submit-button']").click()

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert.accept()
        print("alert says:", alert.text)
        alert.accept()
    except:
        print("⚠️ No alert appeared.")
    WebDriverWait(driver, 5)
    driver.find_element(By.LINK_TEXT, "Test Cases").click()
