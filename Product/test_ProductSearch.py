from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_search(browserInstance):
    ProductSearch(browserInstance)


def ProductSearch(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()
    driver.find_element(By.ID, "search_product").send_keys("T-Shirt")
    driver.find_element(By.CSS_SELECTOR, "#submit_search").click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".features_items h2")))
    assert "SEARCHED PRODUCTS" in driver.find_element(By.CSS_SELECTOR, ".features_items h2").text
    product_name = driver.find_elements(By.CSS_SELECTOR, ".productinfo.text-center p")
    search_item = "T-Shirt".lower()
    assert len(product_name)>0, "list is empty"

    for search in product_name:
        search_name = search.text.lower()
        assert search_item in search_name, f"product{search.text} is not present"

