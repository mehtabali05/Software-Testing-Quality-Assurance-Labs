
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open HTML Forms page
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    # Find all text input elements using CSS Selector
    text_inputs = driver.find_elements(
        By.CSS_SELECTOR, "input[type='text']"
    )

    # Print total matching elements
    print("Total Text Inputs:", len(text_inputs))

    # Print identifying attributes
    for index, field in enumerate(text_inputs, start=1):
        field_id = field.get_attribute("id")
        field_name = field.get_attribute("name")

        print(
            f"Input {index}: ID={field_id}, Name={field_name}"
        )

finally:
    # Close browser
    driver.quit()
