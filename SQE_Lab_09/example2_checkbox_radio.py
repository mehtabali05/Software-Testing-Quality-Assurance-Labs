from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open Selenium practice form
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate checkbox by ID
    checkbox = driver.find_element(By.ID, "my-check-2")

    # Check initial state
    print("Initial Checkbox State:", checkbox.is_selected())

    # Click checkbox
    checkbox.click()

    # Check state after clicking
    print("After Clicking:", checkbox.is_selected())

    # Locate radio button by ID and click it
    radio = driver.find_element(By.ID, "my-radio-2")
    radio.click()

    # Verify radio button state
    print("Radio Selected:", radio.is_selected())

finally:
    driver.quit()