
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    # Open Selenium practice form
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate dropdown
    dropdown_element = driver.find_element(
        By.NAME, "my-select"
    )

    # Create Select object
    dropdown = Select(dropdown_element)

    # Select by visible text
    dropdown.select_by_visible_text("Two")

    print(
        "Selected by Visible Text:",
        dropdown.first_selected_option.text
    )

    # Select by index
    dropdown.select_by_index(3)

    print(
        "Selected by Index:",
        dropdown.first_selected_option.text
    )

    # Select by value
    dropdown.select_by_value("1")

    print(
        "Selected by Value:",
        dropdown.first_selected_option.text
    )

finally:
    # Close browser
    driver.quit()
