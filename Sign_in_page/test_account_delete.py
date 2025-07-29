from selenium.webdriver.common.by import By


def acc_delete(driver):
    # delete account
    driver.find_element(By.CSS_SELECTOR, "a[href= '/delete_account']").click()
    delete_account = driver.find_element(By.CSS_SELECTOR, "h2[data-qa= 'account-deleted']").text
    assert "ACCOUNT DELETED!" in delete_account.strip()
