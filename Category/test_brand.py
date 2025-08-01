from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_brand(browserInstance):
    brand_page(browserInstance)


def brand_page(driver):
    # navigating to product page
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()

    # asserting to verify if on correct part
    assert "BRANDS" in driver.find_element(By.CSS_SELECTOR, "div[class= 'brands_products'] h2").text

    # clicking into the subcategories in brand to navigate to next page
    action = ActionChains(driver)
    brand_polo = driver.find_element(By.CSS_SELECTOR, "div[class= 'brands-name'] ul a[href='/brand_products/Polo']")
    action.click(brand_polo).perform()

    # asserting to verify if navigated to correct page
    assert "POLO" in driver.find_element(By.CSS_SELECTOR, ".title.text-center").text

    # navigating to another page
    Brand_hm = driver.find_element(By.CSS_SELECTOR, "a[href='/brand_products/H&M']")
    action.click(Brand_hm).perform()

    assert "H&M" in driver.find_element(By.CSS_SELECTOR, ".title.text-center").text
