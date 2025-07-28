from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def personal_info(driver):
    # personal info register(new page login 2)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='id_gender1']")))
    driver.find_element(By.CSS_SELECTOR, "input[id='id_gender1']").click()
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("as")
    driver.find_element(By.XPATH, "//select[@id='days']/option[@value='10']").click()
    driver.find_element(By.CSS_SELECTOR, "select[id='months'] option[value='2']").click()
    driver.find_element(By.CSS_SELECTOR, "select[name='years'] option[value='2004']").click()
    driver.find_element(By.CSS_SELECTOR, "#newsletter").click()
    driver.find_element(By.CSS_SELECTOR, "#optin").click()
    driver.find_element(By.CSS_SELECTOR, "#first_name").send_keys("Udit")
    driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Singh")
    driver.find_element(By.NAME, "company").send_keys("Fresher")
    driver.find_element(By.CSS_SELECTOR, "#country").send_keys("I")
    driver.find_element(By.XPATH, "//select[@id='country']/option[@value='India']").click()
    driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Aligarh")
    driver.find_element(By.ID, "state").send_keys("Uttar Pradesh")
    driver.find_element(By.XPATH, "//input[@name='zipcode']").send_keys("202001")
    driver.find_element(By.CSS_SELECTOR, "#mobile_number").send_keys("9258192581")
    driver.find_element(By.CSS_SELECTOR, "#address1").send_keys("Gandhi Nagar")
    driver.find_element(By.XPATH, "//input[@id = 'address2']").send_keys("that's it")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()
   #print(driver.find_element(By.CSS_SELECTOR, "h2[class='title text-center'] b").text)
    assert "ACCOUNT CREATED!" in driver.find_element(By.CSS_SELECTOR, "h2[class='title text-center'] b").text
    driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
    #driver.find_element(By.CSS_SELECTOR, "a[href= '/delete_account']").click()
