
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open W3Schools Forms page
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    # Locate element using ID
    elem_id = driver.find_element(By.ID, "fname")
    print("Found by ID:", elem_id.get_attribute("placeholder"))

    # Locate all links using Tag Name
    links = driver.find_elements(By.TAG_NAME, "a")
    print("Total links on page:", len(links))

    # Locate submit button using CSS Selector
    btn = driver.find_element(
        By.CSS_SELECTOR, 'input[type="submit"]'
    )
    print("Button found:", btn.get_attribute("value"))

finally:
    driver.quit()
