
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open login page
    driver.get(
        "https://practicetestautomation.com/practice-test-login/"
    )

    # 1. Locate using ID
    username_id = driver.find_element(
        By.ID, "username"
    )
    print("Username field found using ID.")

    # 2. Locate using NAME
    username_name = driver.find_element(
        By.NAME, "username"
    )
    print("Username field found using NAME.")

    # 3. Locate using CSS Selector
    username_css = driver.find_element(
        By.CSS_SELECTOR, "input[name='username']"
    )
    print("Username field found using CSS Selector.")

finally:
    # Close browser
    driver.quit()
