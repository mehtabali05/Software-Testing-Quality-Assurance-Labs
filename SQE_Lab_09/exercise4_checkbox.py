
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open practice form
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate checkbox
    checkbox = driver.find_element(By.ID, "my-check-1")

    # Record initial state
    initial_state = checkbox.is_selected()
    print("Initial State:", initial_state)

    # First click
    checkbox.click()

    after_first_click = checkbox.is_selected()
    print("After First Click:", after_first_click)

    # Second click
    checkbox.click()

    after_second_click = checkbox.is_selected()
    print("After Second Click:", after_second_click)

    # Verify results
    print("First Click Changed State:", after_first_click != initial_state)

    print("Second Click Restored State:", after_second_click == initial_state)

finally:
    # Close browser
    driver.quit()
