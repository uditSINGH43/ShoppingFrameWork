from selenium.webdriver.common.by import By

from reviewCart.test_reviewPage import reviewpage


def test_review(browserInstance):
    review(browserInstance)


def review(driver):
    # going to product page
    driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()

    # asserting to view if landed on correct page
    assert "ALL PRODUCTS" in driver.find_element(By.CSS_SELECTOR, ".title.text-center").text

    # clicking on product_details button
    driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()

    # validating 'write review is vissible'
    review = driver.find_element(By.CSS_SELECTOR, "a[href='#reviews']")
    assert "WRITE YOUR REVIEW" in review.text

    # entering details and review
    reviewpage(driver)
