from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_category(browserInstance):
    new_category(browserInstance)


def new_category(driver):
    assert "Automation Exercise" in driver.title  # asserting title of page
    action = ActionChains(driver)

    # naviagting to 'span' child tag of 'woman' class
    action.move_to_element(
        driver.find_element(By.XPATH, "//a[normalize-space()='Women']/child::span")).click().perform()
    wait = WebDriverWait(driver, 10)

    # selecting category woman -> dress
    dress_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category_products/1']")))
    action.move_to_element(dress_button).click().perform()
    dress_text = (driver.find_element(By.CSS_SELECTOR, ".title.text-center"))
    assert "WOMEN - DRESS PRODUCTS" in dress_text.text  # asserting to verify if on correct page

    # naviagting to new page man -> tshirts
    men_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#Men']")))
    action.move_to_element(men_menu).click().perform()

    tshirts_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "TSHIRTS")))
    action.move_to_element(tshirts_link).click().perform()

    assert "MEN - TSHIRTS PRODUCTS" in driver.find_element(By.CSS_SELECTOR,
                                                           ".title.text-center").text  # asserting to verify
