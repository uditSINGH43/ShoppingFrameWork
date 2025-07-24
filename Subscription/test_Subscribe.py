from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_subscribe(browserInstance):
    subs(browserInstance)

def subs(driver):
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#susbscribe_email")).click().perform()
    action.send_keys("2004asbidb@gmail.com").perform()
    action.click(driver.find_element(By.CSS_SELECTOR, "button[id='subscribe']")).click().perform()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='alert-success alert']")))
    assert "You have been successfully subscribed!" in driver.find_element(By.CSS_SELECTOR, "div[class='alert-success alert']").text


