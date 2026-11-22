
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

try:
    # Open HTML Tables page
    driver.get("https://www.w3schools.com/html/html_tables.asp")

    # XPath expression
    xpath = "//table[.//th[normalize-space()='Company']]//tr[3]/td[2]"

    # Locate the table cell
    cell = driver.find_element(By.XPATH, xpath)

    # Print cell text
    print("Located Table Cell:", cell.text)

finally:
    # Close browser
    driver.quit()
