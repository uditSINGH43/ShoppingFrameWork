from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_recommendation(browserInstance):
    recommend(browserInstance)

def recommend(driver):
    #asserting and navigating 'recommending item' part of 'home page'
    reco = driver.find_element(By.CSS_SELECTOR, "div[class='recommended_items'] h2[class='title text-center']")
    assert "RECOMMENDED ITEMS" in reco.text
    # clicking on the cart button on recommended item section (hate that css_selector but no choice at moment)
    wait = WebDriverWait(driver, 10)
    item_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4)")))
    actions = ActionChains(driver)
    actions.move_to_element(item_cart).click().perform()

    #going to cart
    driver.find_element(By.XPATH, "//u[normalize-space()='View Cart']").click()

    #asserting to get verify the corect product is added
    dress = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/3']")
    assert "Sleeveless Dress" in dress.text




