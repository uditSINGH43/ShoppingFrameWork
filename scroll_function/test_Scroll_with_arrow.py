import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scroll(browserInstance):
    scroll(browserInstance)


def scroll(driver):
    # Step 1: Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for UI animation if any

    # Step 2: Click 'Scroll Up' arrow button
    wait = WebDriverWait(driver, 10)
    arrow_up = wait.until(EC.element_to_be_clickable((By.ID, "scrollUp")))
    arrow_up.click()

    # Step 3: Verify that page is scrolled to top
    wait.until(lambda d: d.execute_script("return window.pageYOffset") == 0)

    print("✅ Scroll up via arrow button successful.")
