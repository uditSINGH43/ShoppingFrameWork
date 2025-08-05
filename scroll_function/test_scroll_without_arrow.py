import time
from selenium.webdriver.support.wait import WebDriverWait


def test_scroll_without_arrow(browserInstance):
    scroll_down(browserInstance)


def scroll_down(driver):
    wait = WebDriverWait(driver, 10)
    # Scroll down a bit
    driver.execute_script("window.scrollBy(0, 1000);")

    # Scroll back to top without clicking arrow
    driver.execute_script("window.scrollTo(0, 0);")

    # Verify scroll position
    wait.until(lambda d: d.execute_script("return window.pageYOffset") == 0)

    print("✅ Scroll up without arrow button successful.")
